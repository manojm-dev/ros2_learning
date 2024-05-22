#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class Addition_Service(Node):

    def __init__(self):
        super().__init__("add_two_ints_service")
        self.service_ = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.add_two_ints_callback
        )

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incomming request \na:{request.a} b:{request.b}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Addition_Service()
    rclpy.spin(node)
    node.destroy_nodes()
    rclpy.shutdown()

if __name__ =="__main__":
    main()
