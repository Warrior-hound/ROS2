import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from conveyorbelt_msgs.srv import ConveyorBeltControl
from conveyorbelt_msgs.msg import ConveyorBeltState
import cv2
from cv_bridge import CvBridge
import numpy as np
from functools import partial

class ImageReader(Node):
    def __init__(self):
        super().__init__('image_reader')
        self.declare_parameter("number", "1")
        self.sensor_number = self.get_parameter("number").value
        
        self.subscription = self.create_subscription(
            Image,
            f'scanner_{self.sensor_number}/camera/image_raw',
            self.process_image,
            10)
        self.subscription  # prevent unused variable warning
        self.subscription_joint = self.create_subscription(
            ConveyorBeltState,
            f'pusher_{self.sensor_number}/PRISMATICSTATE',
            self.process_current_velocity,
            10)
        self.get_zone_subscription = self.create_subscription(
            Bool,
            f'ir{((int(self.sensor_number) - 1) * 6) + 1}/currently_at_conveyor',
            self.get_zone_callback,
            10)
    

        self.subscription_joint
        self.br = CvBridge()
        self.was_turning_to = 'left'
        self.prev_cx = None
        self.prev_cy = None
        self.should_push = False
        self.is_pushing = False

    def get_zone_callback(self, msg):
        self.should_push = msg.data
        
    

    def process_image(self, msg):
        current_frame = self.br.imgmsg_to_cv2(msg)
        
        # Convert to HSV color space
        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
        
        # Define range for blue color in HSV
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([130, 255, 255])
        
        # Create a mask for blue color
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        frame_height, frame_width, _ = current_frame.shape
        center_x, center_y = frame_width // 2, frame_height // 2
        center_region_size = 5 
        center_x -= 83
        for contour in contours:
        # Get bounding box for each contour
            (x, y, w, h) = cv2.boundingRect(contour)
            
            # Define criteria for the box (e.g., size range)
            if center_x - center_region_size < x < center_x + center_region_size:
                cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(current_frame, f"W:{w} H:{h}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                self.push_pusher()
            else:
                cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(current_frame, f"W:{w} H:{h}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
 
        if ((int(self.sensor_number) - 1) * 6) + 1 == 7:
            cv2.imshow(f"camera_{((int(self.sensor_number) - 1) * 6) + 1}", current_frame)
        cv2.waitKey(1)


    def push_pusher(self):
            if not self.should_push:
                return
            client = self.create_client(ConveyorBeltControl, f'pusher_{self.sensor_number}/perform_stroke')
            while not client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('Service not available, waiting again...')
            request = ConveyorBeltControl.Request()
            request.power = 1.0
            
            future = client.call_async(request)
         
            future.add_done_callback(partial(self.callback_call_push_pusher))

    def callback_call_push_pusher(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Service call succeeded: {response}')
        except Exception as e:
            self.get_logger().error('Service call failed %r' % (e,))

    def process_current_velocity(self, msg):
            self.current_velocity = msg.power
           

def crop_size(height, width):
    return (height // 6, height, width // 8, 7 * width // 8)

def main(args=None):
    rclpy.init(args=args)

    image_reader = ImageReader()

    rclpy.spin(image_reader)

    image_reader.destroy_node()
    rclpy.shutdown()