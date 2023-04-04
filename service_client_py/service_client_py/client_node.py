import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class AdditionClientAsync(Node):

    def __init__(self):
        super().__init__("add_two_client_async")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, retrying ...")

    def send_request(self):
        request = AddTwoInts.Request()
        request.a = int(sys.argv[1])
        request.b = int(sys.argv[2])
        self.future = self.client_.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    client_node = AdditionClientAsync()
    client_node.send_request()

    while rclpy.ok():
        rclpy.spin_once(client_node)
        if client_node.future.done():
            try:
                response = client_node.future.result()
            except Exception as e:
                client_node.get_logger().info( f"service call failed {e}")
            else:
                client_node.get_logger().info(f"The result of addition is {response.sum}")
            break
        client_node.destroy_node()
        rclpy.shutdown()

if __name__=="__main__":
    main()