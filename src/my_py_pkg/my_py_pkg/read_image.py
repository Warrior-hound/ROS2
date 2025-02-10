import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import cv2
from cv_bridge import CvBridge
import numpy as np


class ImageReader(Node):

    def __init__(self):
        super().__init__('image_reader')
        self.get_logger().info('Image reader has been started')
        self.subscription = self.create_subscription(
            Image,
            'camera_sensor/image_raw',
            self.process_image,
            10)
        self.br = CvBridge()
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # PID controller parameters
        self.kp = 0.01
        self.ki = 0.000009
        self.kd = 0.004
        self.prev_error = 0
        self.integral = 0
        
        # Initial speed
        self.base_speed = 0.2
        self.max_speed = 0.2
        self.speed_increment = 0.001
        self.was_turning_to = 'left'
        # Previous centroid
        self.prev_cx = None
        self.prev_cy = None

    def process_image(self, msg):
        current_frame = self.br.imgmsg_to_cv2(msg)
        # crop the image
        height, width, _ = current_frame.shape
        print(height, width)
        crop_h_start, crop_h_stop, crop_w_start, crop_w_stop = crop_size(height, width)
        # current_frame = current_frame[crop_h_start:crop_h_stop, crop_w_start:crop_w_stop]
        current_frame = cv2.bitwise_not(current_frame)
        kernel = np.ones((25,25), np.uint8)
        current_frame = cv2.erode(current_frame, kernel, iterations=1)

        # Convert to grayscale
        gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        # Threshold the image
        ret,thresh = cv2.threshold(gray, 127, 255, 0)
        # Find contours
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Draw contours
        cv2.drawContours(current_frame, contours, -1, (0,255,0), 3)
        # smooth the contours
        good_contours = []
        for cnt in contours:
            epsilon = 0.02*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            good_contours.append(approx)
            cv2.drawContours(current_frame, [approx], -1, (255, 0, 0), 3)

        # Find the centroid of the largest contour

        if len(good_contours) > 0:
            c = max(good_contours, key=cv2.contourArea)
            # if area is too small, ignore
            if cv2.contourArea(c) < 200:
                return
            M = cv2.moments(c)
            angular_z = 0.0
            error = 0
            cx = 0
            cy = 0
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.circle(current_frame, (cx, cy), 7, (0, 0, 255), -1)
                cv2.putText(current_frame, f"centroid: ({cx}, {cy})", (cx - 50, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        # PID controller
                error = cx - 320
                self.integral += error
                kp_speed = -self.kp * error
                ki_speed = self.ki * self.integral
                kd_speed = self.kd * (error - self.prev_error)
                angular_z = kp_speed + ki_speed + kd_speed

            self.was_turning_to = 'left' if angular_z < 0 else 'right'
            # + self.ki * self.integral + self.kd * (error - self.prev_error)
            self.prev_error = error
            # Publish the velocity
            msg = Twist()
            msg.linear.x = self.base_speed
            msg.angular.z = angular_z
            self.publisher.publish(msg)
            self.get_logger().info(f'Kp: {kp_speed}, Ki: {ki_speed}, Kd: {kd_speed} Error: {error}')
            self.prev_cx = cx
            self.prev_cy = cy
        else:
            msg = Twist()
            msg.linear.x = 0.0
            # if was turning left continue turning left
            if self.was_turning_to == 'left':
                msg.angular.z = 0.8
            else:
                msg.angular.z = -0.8
            self.publisher.publish(msg)
            self.get_logger().info("No contours found")
            self.prev_cx = None
            self.prev_cy = None
        cv2.imshow("camera", current_frame)


        
        cv2.waitKey(1)
    


def crop_size(height, width):
    return (height // 4, height, width // 6, 5 * width // 6)

    
def main(args=None):
    rclpy.init(args=args)

    image_reader = ImageReader()

    rclpy.spin(image_reader)

    image_reader.destroy_node()
    rclpy.shutdown()
