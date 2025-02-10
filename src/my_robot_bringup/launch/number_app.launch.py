from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    number_publisher_node = Node(
        package="my_py_pkg",
        executable="number_counter",
    )

    counter_node = Node(
        package="my_cpp_pkg",
        executable="number_publisher",
    )



    ld.add_action(number_publisher_node)
    ld.add_action(counter_node)

    return ld