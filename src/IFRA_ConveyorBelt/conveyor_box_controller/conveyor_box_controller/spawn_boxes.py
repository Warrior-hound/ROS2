import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity
from std_msgs.msg import String
import os
from ament_index_python.packages import get_package_share_directory
import xacro

class BoxSpawner(Node):

    def __init__(self):
        super().__init__('box_spawner')
        self.client = self.create_client(SpawnEntity, '/spawn_entity')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.num_of_boxes = 0
        self.publisher = self.create_publisher(String, 'box_spawn_status', 10)
        self.timer = self.create_timer(10.0, self.spawn_box)  # Timer to call spawn_box every 4 seconds
   

    def spawn_box(self):
        if self.num_of_boxes == 1:
            return
        request = SpawnEntity.Request()
        request.name = 'box' + str(self.num_of_boxes)
        urdf_file_path = os.path.join(get_package_share_directory('conveyorbelt_gazebo'), 'urdf', 'box.urdf')
        xacro_file = xacro.process_file(urdf_file_path)
        request.xml = xacro_file.toxml() 
        # 42.375 -1.320
        request.initial_pose.position.x = float(-47)
        request.initial_pose.position.y = float(0)
        request.initial_pose.position.z = float(0.31)

        self.get_logger().info('Spawning OBJECT using service: `/spawn_entity`')
        future = self.client.call_async(request)
        future.add_done_callback(self.spawn_box_callback)
        self.spawned = True

    def spawn_box_callback(self, future):
        try:
            response = future.result()
            self.publisher.publish(String(data='Ok'))
            self.num_of_boxes += 1
            
        except Exception as e:
            self.get_logger().error('Service call failed %r' % (e,))

def main(args=None):
    rclpy.init(args=args)
    box_spawner = BoxSpawner()
    rclpy.spin(box_spawner)
    box_spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()