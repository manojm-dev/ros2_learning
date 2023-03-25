import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class GetItemsFromFarmers(Node):
    
    def __init__(self):
        super().__init__("shop")
        self.shop = self.create_subscription(String,"/farmer1_items",self.getitem_callback,10)

    def getitem_callback(self,msg: String):
        self.get_logger().info(str(msg.data)+" is received")

def main(args=None):
    rclpy.init(args=args)
    shop = GetItemsFromFarmers()
    rclpy.spin(shop)
    shop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()