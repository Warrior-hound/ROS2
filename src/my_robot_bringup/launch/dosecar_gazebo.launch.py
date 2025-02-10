from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path



def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path('my_robot_description'), 'urdf', 'dosecar.urdf.xacro')

    rviz_config_path = os.path.join(get_package_share_path('my_robot_bringup'),
                                    'rviz', 'urdf_config.rviz')
    
    world_path = os.path.join(get_package_share_path('my_robot_bringup'), 'worlds', 'trial.world')

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', urdf_path])}]
    )

    gazebo_launch_path = os.path.join(get_package_share_path('gazebo_ros'), 'launch', 'gazebo.launch.py')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_path),
        launch_arguments={'world': world_path}.items()
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'dosecar']
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', '/home/meditab/Desktop/ROS2/src/my_robot_bringup/rviz/urdf_config.rviz'],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawn_entity,
        rviz_node
    ])

    