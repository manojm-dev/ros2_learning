#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Draw_circle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(0.5,self.send_vel_cmd)
        self.get_logger().info("Draw Circle has been initiated")

    def send_vel_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Draw_circle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== '__main__':
    main()