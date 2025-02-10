import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity
from std_msgs.msg import String
from conveyorbelt_msgs.srv import PusherControl
import os
from ament_index_python.packages import get_package_share_directory
import xacro

class StickerSpawner(Node):

    def __init__(self):
        super().__init__('sticker_spawner')
        self.declare_parameter("sensor_names", "ir1 ir2 ir3 ir4 ir5 ir6")
        self.sensor_names = self.get_parameter("sensor_names").value
        self.split_sensor_names = self.sensor_names.split()
        self.client = self.create_client(SpawnEntity, '/spawn_entity')
        # self.joint_client = self.create_client(SetModelConfiguration, '/gazebo/set_model_configuration')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.num_of_stickers = 0
        self.publisher = self.create_publisher(String, 'sticker_spawn_status', 10)
        self.service = self.create_service(PusherControl, f'/spawner_{map_sensor_number(int(self.split_sensor_names[0][2:]))}/spawn_sticker', self.spawn_sticker)
   

    def spawn_sticker(self, req, res):
        request = SpawnEntity.Request()
        request.name = 'sticker' + str(self.num_of_stickers)
        urdf_file_path = os.path.join(get_package_share_directory('conveyorbelt_gazebo'), 'urdf', 'sticker.urdf')
        xacro_file = xacro.process_file(urdf_file_path)
        request.xml = xacro_file.toxml() 
        # 42.375 -1.320
        request.initial_pose.position.x = float(-30.395730)
        request.initial_pose.position.y = float(-1.967942)
        request.initial_pose.position.z = float(0.303000)

        self.get_logger().info('Spawning sticker using service: `/spawn_entity`')
        future = self.client.call_async(request)
        future.add_done_callback(self.spawn_sticker_callback)
        self.spawned = True

        # self.get_logger().info('Creating fixed joint now')
        res.success = True
        return res

    def spawn_sticker_callback(self, future):
        try:
            response = future.result()
            self.publisher.publish(String(data='Ok'))
            self.num_of_stickers += 1
            
        except Exception as e:
            self.get_logger().error('Service call failed %r' % (e,))

def map_sensor_number(sensor_number):
    if sensor_number % 6 == 1:
        return (sensor_number // 6) + 1
    else:
        return None  # or handle other cases if needed

def main(args=None):
    rclpy.init(args=args)
    sticker_spawner = StickerSpawner()
    rclpy.spin(sticker_spawner)
    sticker_spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()