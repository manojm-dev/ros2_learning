#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("First_Node")
        self.counter=0
        self.create_timer(0.5,self.hello)

    def hello(self):
        self.get_logger().info("Hello "+ str(self.counter))
        self.counter+=1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__== '__main__':
    main()
