#!/usr/bin/env python
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__('add_two_ints_server')
        self.server = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Add Two Ints Server has been started')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response
    
def main(args=None):
    rclpy.init(args=args)
    add_two_ints_server = AddTwoIntsServer()
    rclpy.spin(add_two_ints_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()