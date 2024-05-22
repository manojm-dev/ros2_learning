import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FarmerItemPublisher(Node):

    def __init__(self):
        super().__init__("farmer_2")
        self.farmer2 = self.create_publisher(String,"/item/farmer2",10)
        self.create_timer(1.0,self.pub_callback)

    def pub_callback(self):
        msg = String()
        msg.data = "orange"
        self.farmer2.publish(msg)
        self.get_logger().info("farmer 2 is transporting "+str(msg.data))

def main(args=None):
    rclpy.init(args=args)
    item_publisher = FarmerItemPublisher()
    rclpy.spin(item_publisher)
    item_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()