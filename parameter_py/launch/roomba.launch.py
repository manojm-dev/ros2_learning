from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    roomba = Node(
        package = 'parameter_py',
        executable = 'roomba_node',
        name = 'roomba_node_1',
        output = 'screen',
        emulate_tty = True,
        parameters=[
        {'roomba_mode' : 'sweep'}
        ]
    )