#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import SetLed
from functools import partial


class Battery(Node):
    def __init__(self):
        super().__init__("battery")
        self.battery_state = 100
        self.time_elapsed = 0
        self.get_logger().info("Battery powering up")
        self.create_timer(1, self.timer_callback)
    
    def timer_callback(self):
        self.time_elapsed += 1
        if self.time_elapsed % 4 and self.battery_state > 0:
            self.battery_state = 0
            self.call_set_led_server(turn_on_off=True)
        elif self.time_elapsed % 10 and self.battery_state < 100:
            self.battery_state = 100
            self.call_set_led_server(turn_on_off=False)
        
    def call_set_led_server(self, turn_on_off):
        client = self.create_client(SetLed, 'set_led_status')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting again...')
        
        request = SetLed.Request()
        request.turn_on_off = turn_on_off
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led, turn_on_off=turn_on_off))
    
    def callback_call_set_led(self, future, turn_on_off):
        try:
            response = future.result()
            self.get_logger().info('Status: %r' % response.status)
        except Exception as e:
            self.get_logger().error('Service call failed %r' % e)


def main(args=None):
    rclpy.init(args=args)
    node = Battery()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()