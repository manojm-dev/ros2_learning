from launch import LaunchDescription
from launch_ros.actions import Node 

def generate_launch_description():
    farmer1 = Node(
        package="pub_sub_py",
        executable="farmer1",
        name = "farmer_1",
    )
    
    farmer2 = Node(
        package="pub_sub_py",
        executable="farmer2",
        name="farmer_2",
    )

    shop = Node(
        package="pub_sub_py",
        executable="shop",
        name="shop",
    )

    return LaunchDescription([
        farmer1,
        farmer2,
        shop
    ])
