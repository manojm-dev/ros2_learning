import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FarmerItemPublisher(Node):

    def __init__(self):
        super().__init__("farmer_1")
        self.farmer1 = self.create_publisher(String,"item/farmer1",10)
        self.create_timer(1.0,self.pub_callback)

    def pub_callback(self):
        msg = String()
        msg.data = "apple"
        self.farmer1.publish(msg)
        self.get_logger().info("farmer1 is transporting "+ str(msg.data))

def main(args=None):
    rclpy.init(args=args)
    item_publisher = FarmerItemPublisher()
    rclpy.spin(item_publisher)
    item_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()