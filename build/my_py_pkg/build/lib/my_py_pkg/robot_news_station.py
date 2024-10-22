#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class RobotNewsStation(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.declare_parameter("robot_name", "HOUND")
        self.robot_name_ = self.get_parameter("robot_name").value
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info(f"{self.robot_name_} News Station is live!")

    def publish_news(self):
        msg = String()
        random_news = ["I am a robot", "Hello, Robot", "Robot is working"]
        msg.data = random_news[random.randint(0, len(random_news)- 1)]
        self.publisher_.publish(msg)
        
        


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()