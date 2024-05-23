from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="cpp_parameters",
            executable="roomba_node",
            name="roomba_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"roomba_mode": "idle"}
            ]
        )
    ])