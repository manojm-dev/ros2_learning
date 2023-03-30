#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose

class Posesub(Node):

    def __init__(self):
        super().__init__("Pose_Subsriber")
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.sub_pose, 10)
        self.get_logger().info("Intiated Pose subsriber node")

    def sub_pose(self, msg:Pose):
        self.get_logger().info( "(" + str(msg.x) + "," + str(msg.y) + ")" )
        
def main(args=None):
    rclpy.init(args=args)
    node = Posesub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()