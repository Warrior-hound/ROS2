#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedStatus
from my_robot_interfaces.srv import SetLed

class Led(Node):
    def __init__(self):
        super().__init__("led")
        self.status = [0, 0, 0]
        self.get_logger().info("Hello, World!")
        self.publisher = self.create_publisher(LedStatus, "led_status", 10)
        self.service = self.create_service(SetLed, "set_led_status", self.callback)
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = LedStatus()
        msg.led_status = [self.status[0], self.status[1], self.status[2]]
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.led_status}")

    def callback(self, request, response):
        self.get_logger().info(f"Received: {request.turn_on_off}")
        if (request.turn_on_off):
            response.status = True
            self.status = [1, 1, 1]
            self.get_logger().info("LEDs turned on")
            return response
        else:
            response.status = False
            self.status = [0, 0, 0]
            self.get_logger().info("LEDs turned off")
            return response

def main(args=None):
    rclpy.init(args=args)
    node = Led()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()