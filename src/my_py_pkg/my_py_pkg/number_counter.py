import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):

    def __init__(self):
        super().__init__('number_counter')
        self.get_logger().info('Number Counter has been started')
        self.counter = 0
        self.subscription = self.create_subscription(
            Int64,
            'number',
            self.number_callback,
            10)
        self.subscription
        self.publisher = self.create_publisher(Int64, 'number_count', 10)
        self.service = self.create_service(SetBool, 'reset_counter', self.reset_counter_callback)

    def number_callback(self, msg):
        publish_msg = Int64()
        self.counter += msg.data
        publish_msg.data = self.counter
        self.publisher.publish(publish_msg)
        # self.get_logger().info('Counter: %d' % self.counter)

    def reset_counter_callback(self, request, response):
        if (request.data == True):
            self.counter = 0
            response.success = True
            response.message = 'Counter has been reset'
            self.get_logger().info('Counter has been reset')
            return response
        else:
            response.success = False
            response.message = 'Counter has not been reset'
            self.get_logger().info('Counter has not been reset')
            return response
    
    
    



def main(args=None):
    rclpy.init(args=args)

    number_counter = NumberCounter()

    rclpy.spin(number_counter)

    number_counter.destroy_node()
    rclpy.shutdown()
