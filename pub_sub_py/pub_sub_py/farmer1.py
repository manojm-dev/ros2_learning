import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublishItems(Node):

    def __init__(self):
        super().__init__("farmer_1")
        self.pub_farmer = self.create_publisher(String, "/farmer1_items",10)
        self.create_timer(1.0,self.item_callback)

    def item_callback(self):
        item = String()
        item.data = "apples"
        self.pub_farmer.publish(item)
        self.get_logger().info("Farmer1 is sending "+ str(item.data)+ " to the shop")

def main(args=None):
    rclpy.init(args=args)
    farmer_1 = PublishItems()
    rclpy.spin(farmer_1)
    farmer_1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main___':
    main()