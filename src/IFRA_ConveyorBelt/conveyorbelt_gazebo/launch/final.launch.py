import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Gazebo launch file
    to_launch = []
    conveyorbelt_gazebo = os.path.join(
        get_package_share_directory('conveyorbelt_gazebo'),
        'worlds',
        'test.world'
    )
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
        launch_arguments={'world': conveyorbelt_gazebo}.items(),
    )

    to_launch.append(gazebo)
    # Nodes to run
    conveyor_starter = Node(
        package='conveyor_box_controller',
        executable='conveyor_starter',
        name='conveyor_starter',
        output='screen'
    )

    to_launch.append(conveyor_starter)
    

    # open 5 nodes of read_image
    for i in range(1, 6):
        print(i)
        read_image = Node(
            package='conveyor_box_controller',
            executable='read_image',
            name=f'read_image_{i}',
            output='screen',
            parameters=[{'number': str(i)}]
        )
        to_launch.append(read_image)
    

    


    # open 5 nodes of control_medium_conveyor
    for i in range(1, 6):
        sensor_names = [
            1 + (6 * (i - 1)),
            2 + (6 * (i - 1)),
            3 + (6 * (i - 1)),
            4 + (6 * (i - 1)),
            5 + (6 * (i - 1)),
            6 + (6 * (i - 1))
        ]
        print(sensor_names)
        control_medium_conveyor = Node(
            package='conveyor_box_controller',
            executable='control_medium_conveyor',
            name=f'control_medium_conveyor_{i}',
            output='screen',
            parameters=[{'sensor_names': ' '.join([f'ir{sensor}' for sensor in sensor_names])}]
        )
        sticker_spawner = Node(
            package='conveyor_box_controller',
            executable='spawn_stickers',
            name=f'sticker_spawner_{i}',
            output='screen',
            parameters=[{'sensor_names': ' '.join([f'ir{sensor}' for sensor in sensor_names])}]
        )
        to_launch.append(control_medium_conveyor)
        to_launch.append(sticker_spawner)

    

    
    spawn_boxes = Node(
        package='conveyor_box_controller',
        executable='spawn_boxes',
        name='spawn_boxes',
        output='screen'
    )
    
    to_launch.append(spawn_boxes)
   

                     

    return LaunchDescription(to_launch)