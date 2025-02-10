import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from conveyorbelt_msgs.srv import ConveyorBeltControl
from conveyorbelt_msgs.srv import PusherControl
from conveyorbelt_msgs.msg import ConveyorBeltState
import cv2
from cv_bridge import CvBridge
import numpy as np
from functools import partial
from sensor_msgs.msg import Range

class ControlMediumConveyor(Node):
    def __init__(self):
        super().__init__('control_medium')
        self.declare_parameter("sensor_names", "ir1 ir2 ir3 ir4 ir5 ir6")
        self.sensor_names = self.get_parameter("sensor_names").value
        self.split_sensor_names = self.sensor_names.split()
        self.currently_at_conveyor = 0
        self.client_1 = self.create_client(ConveyorBeltControl, '/primary_conveyor/CONVEYORPOWER')
        self.subscription_1 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[0]}/range',
            self.process_sensor_1,
            10)
        self.subscription_2 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[1]}/range',
            self.process_sensor_2,
            10)
        self.subscription_3 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[2]}/range',
            self.process_sensor_3,
            10)
        self.subscription_4 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[3]}/range',
            self.process_sensor_4,
            10)
        self.subscription_5 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[4]}/range',
            self.process_sensor_5,
            10)
        self.subscription_6 = self.create_subscription(
            Range,
            f'{self.split_sensor_names[5]}/range',
            self.process_sensor_6,
            10)
        self.position_at = [0, 0, 0, 0, 0, 0]
        print(f'{self.split_sensor_names}')
        self.big_time = 3.0 #20.0
        self.small_time = 0 #10.0
        self.publisher = self.create_publisher(Bool, f'{self.split_sensor_names[0]}/currently_at_conveyor', 10)


    def process_sensor_1(self, msg):
        status_msg = Bool()
        status_msg.data = False if self.position_at[0] == 1 else True
        self.publisher.publish(status_msg)
      
        if msg.range >= 2.0:
            self.position_at[0] = 0
        if msg.range < 2.0 and self.position_at[0] == 0:
            self.update_conveyor(False, 0)
            self.position_at[0] = 1
            self.create_one_shot_timer(self.big_time, lambda: self.update_conveyor(True, 0))
        
        

    def process_sensor_2(self, msg):
       
        if msg.range >= 2.0:
            self.position_at[1] = 0
        if msg.range < 2.0 and self.position_at[1] == 0:
            self.update_conveyor(False, 1)
            self.position_at[1] = 1
            self.create_one_shot_timer(self.small_time, lambda: self.update_conveyor(True, 1))

    def process_sensor_3(self, msg):
        if msg.range >= 2.0:
            self.position_at[2] = 0
        if msg.range < 2.0 and self.position_at[2] == 0:
            self.update_conveyor(False, 2)
            self.position_at[2] = 1
            self.create_one_shot_timer(self.big_time, lambda: self.update_conveyor(True, 2))

    def process_sensor_4(self, msg):
        if msg.range >= 2.0:
            self.position_at[3] = 0
        if msg.range < 2.0 and self.position_at[3] == 0:
            self.update_conveyor(False, 3)
            self.position_at[3] = 1
            self.create_one_shot_timer(self.big_time, lambda: self.update_conveyor(True, 3))

    def process_sensor_5(self, msg):
        if msg.range >= 2.0:
            self.position_at[4] = 0
        if msg.range < 2.0 and self.position_at[4] == 0:
            self.update_conveyor(False, 4)
            self.position_at[4] = 1
            self.create_one_shot_timer(self.small_time, lambda: self.update_conveyor(True, 4))

    def process_sensor_6(self, msg):
        if msg.range >= 2.0:
            self.position_at[5] = 0
        if msg.range < 2.0 and self.position_at[5] == 0:
            self.update_conveyor(False, 5)
            self.put_sticker()
            self.position_at[5] = 1
            self.create_one_shot_timer(self.small_time, lambda: self.update_conveyor(True, 5))

    def create_one_shot_timer(self, duration, callback):
        timer = self.create_timer(duration, lambda: self.one_shot_timer_callback(timer, callback))

    def one_shot_timer_callback(self, timer, callback):
        timer.cancel()
        callback()

    def put_sticker(self):
        spawner_number = map_sensor_number(int(self.split_sensor_names[0][2:]))
        client = self.create_client(PusherControl, f'/spawner_{spawner_number}/spawn_sticker')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Stickers not available, waiting again...')
        request = PusherControl.Request()
        request.move = True
            
        future = client.call_async(request)
         
        future.add_done_callback(partial(self.callback_call_put_sticker))

    def callback_call_put_sticker(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Sticker placed')
        except Exception as e:
            self.get_logger().error('Service call failed %r' % (e,))



    def update_conveyor(self, start, at):
            conveyor_number = map_sensor_number(int(self.split_sensor_names[0][2:]))
            client = self.create_client(ConveyorBeltControl, f'/medium_line{conveyor_number}/CONVEYORPOWER')
            while not client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('Service not available, waiting again...')
            request = ConveyorBeltControl.Request()
            request.power = 100.00 if start else 0.0
            
            future = client.call_async(request)
         
            future.add_done_callback(partial(self.callback_stop_conveyor, start=start, at=at))

    def callback_stop_conveyor(self, future, start, at):
        try:
            response = future.result()
            self.get_logger().info(f'Conveyor started: {start}')
        except Exception as e:
            self.get_logger().error('Service call failed %r' % (e,))
    
    def currently_at_conveyor(self, msg):
        self.currently_at_conveyor = msg.range

    
           

def crop_size(height, width):
    return (height // 6, height, width // 8, 7 * width // 8)

def map_sensor_number(sensor_number):
    if sensor_number % 6 == 1:
        return (sensor_number // 6) + 1
    else:
        return None  # or handle other cases if needed

def main(args=None):
    rclpy.init(args=args)

    control_medium_conveyor = ControlMediumConveyor()

    rclpy.spin(control_medium_conveyor)

    control_medium_conveyor.destroy_node()
    rclpy.shutdown()