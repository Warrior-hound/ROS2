#!usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node('add_two_ints_client_no_oop')
    
    client = node.create_client(AddTwoInts, 'add_two_ints')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().warn('Service not available, waiting again...')

    request = AddTwoInts.Request()
    
    request.a = 4
    request.b = 5

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    
    if future.result() is not None:
        node.get_logger().info('Sum: %d' % future.result().sum)
    else:
        node.get_logger().error('Service call failed %r' % future.exception())

    rclpy.shutdown()

if __name__ == '__main__':
    main()