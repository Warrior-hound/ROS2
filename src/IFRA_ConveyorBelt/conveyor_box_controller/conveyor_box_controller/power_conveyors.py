import rclpy
from rclpy.node import Node
from conveyorbelt_msgs.srv import ConveyorBeltControl

class BoxSpawner(Node):

    def __init__(self):
        super().__init__('conveyor_starter')
        self.client_1 = self.create_client(ConveyorBeltControl, '/primary_conveyor/CONVEYORPOWER')
        self.client_2 = self.create_client(ConveyorBeltControl, '/secondary_line_1/CONVEYORPOWER')
        self.client_3 = self.create_client(ConveyorBeltControl, '/secondary_line_2/CONVEYORPOWER')
        self.client_4 = self.create_client(ConveyorBeltControl, '/secondary_line_3/CONVEYORPOWER')
        self.client_5 = self.create_client(ConveyorBeltControl, '/secondary_line_4/CONVEYORPOWER')
        self.client_6 = self.create_client(ConveyorBeltControl, '/secondary_line_5/CONVEYORPOWER')
        self.client_7 = self.create_client(ConveyorBeltControl, '/secondary_line_2_1/CONVEYORPOWER')
        self.client_8 = self.create_client(ConveyorBeltControl, '/secondary_line_2_2/CONVEYORPOWER')
        self.client_9 = self.create_client(ConveyorBeltControl, '/secondary_line_2_3/CONVEYORPOWER')
        self.client_10 = self.create_client(ConveyorBeltControl, '/secondary_line_2_4/CONVEYORPOWER')
        self.client_11 = self.create_client(ConveyorBeltControl, '/secondary_line_2_5/CONVEYORPOWER')
          # self.client_4 = self.create_client(ConveyorBeltControl, '/medium_conveyor/CONVEYORPOWER')
        while not self.client_1.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 1 not available, waiting again...')
        while not self.client_2.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 2 not available, waiting again...')
        while not self.client_3.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 3 not available, waiting again...')
        while not self.client_4.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 4 not available, waiting again...')
        while not self.client_5.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 5 not available, waiting again...')
        while not self.client_6.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 6 not available, waiting again...')
        while not self.client_7.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 7 not available, waiting again...')
        while not self.client_8.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 8 not available, waiting again...')
        while not self.client_9.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 9 not available, waiting again...')
        while not self.client_10.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 10 not available, waiting again...')
        while not self.client_11.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service 11 not available, waiting again...')

        self.call_services()

    def call_services(self):
        request = ConveyorBeltControl.Request()
        request.power = 100.00

        future_1 = self.client_1.call_async(request)
        future_2 = self.client_2.call_async(request)
        future_3 = self.client_3.call_async(request)
        future_4 = self.client_4.call_async(request)
        future_5 = self.client_5.call_async(request)
        future_6 = self.client_6.call_async(request)
        future_7 = self.client_7.call_async(request)
        future_8 = self.client_8.call_async(request)
        future_9 = self.client_9.call_async(request)
        future_10 = self.client_10.call_async(request)
        future_11 = self.client_11.call_async(request)

        rclpy.spin_until_future_complete(self, future_1)
        rclpy.spin_until_future_complete(self, future_2)
        rclpy.spin_until_future_complete(self, future_3)
        rclpy.spin_until_future_complete(self, future_4)
        rclpy.spin_until_future_complete(self, future_5)
        rclpy.spin_until_future_complete(self, future_6)
        rclpy.spin_until_future_complete(self, future_7)
        rclpy.spin_until_future_complete(self, future_8)
        rclpy.spin_until_future_complete(self, future_9)
        rclpy.spin_until_future_complete(self, future_10)
        rclpy.spin_until_future_complete(self, future_11)


        if future_1.result() is not None:
            self.get_logger().info('Service 1 call succeeded')
        else:
            self.get_logger().error('Service 1 call failed')

        if future_2.result() is not None:
            self.get_logger().info('Service 2 call succeeded')
        else:
            self.get_logger().error('Service 2 call failed')

        if future_3.result() is not None:
            self.get_logger().info('Service 3 call succeeded')
        else:
            self.get_logger().error('Service 3 call failed')

        if future_4.result() is not None:
            self.get_logger().info('Service 4 call succeeded')
        else:
            self.get_logger().error('Service 4 call failed')

        if future_5.result() is not None:
            self.get_logger().info('Service 5 call succeeded')
        else:
            self.get_logger().error('Service 5 call failed')
        
        if future_6.result() is not None:
            self.get_logger().info('Service 6 call succeeded')
        else:
            self.get_logger().error('Service 6 call failed')

        if future_7.result() is not None:
            self.get_logger().info('Service 7 call succeeded')
        else:
            self.get_logger().error('Service 7 call failed')


        if future_8.result() is not None:
            self.get_logger().info('Service 8 call succeeded')
        else:
            self.get_logger().error('Service 8 call failed')

        if future_9.result() is not None:
            self.get_logger().info('Service 9 call succeeded')
        else:
            self.get_logger().error('Service 9 call failed')

        if future_10.result() is not None:
            self.get_logger().info('Service 10 call succeeded')
        else:
            self.get_logger().error('Service 10 call failed')

        if future_11.result() is not None:
            self.get_logger().info('Service 11 call succeeded')
        else:
            self.get_logger().error('Service 11 call failed')



def main(args=None):
    rclpy.init(args=args)
    box_spawner = BoxSpawner()
    rclpy.spin(box_spawner)
    box_spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()