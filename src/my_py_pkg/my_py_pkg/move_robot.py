#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class MoveRobot(Node):
    def __init__(self):
        super().__init__("move_robot")
        self.publisher_ = self.create_publisher(Twist, "cmd_vel", 10)
        self.timer_ = self.create_timer(0.5, self.publish_velocity)
        self.get_logger().info(f"Velocity commander is live")

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.1
        self.publisher_.publish(msg)

        
        


def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()