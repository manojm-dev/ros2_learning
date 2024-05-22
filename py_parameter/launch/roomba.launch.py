from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    roomba_idle = Node(
        package = 'parameter_py',
        executable = 'roomba',
        name = 'roomba_node_1',
        parameters=[
        {'roomba_mode' : 'sweep'}
        ]
    )

    return LaunchDescription([
        roomba_idle,
    ])