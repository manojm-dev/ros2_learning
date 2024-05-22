import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class FarmerItemSubscriber(Node):

    def __init__(self):
        super().__init__("shop")
        self.farmer1_sub = self.create_subscription(String, "item/farmer1",self.disp_callback,10)
        self.farmer2_sub = self.create_subscription(String, "item/farmer2",self.disp_callback,10)

    def disp_callback(self, msg:String):
        self.get_logger().info(str(msg.data)+" is received")

def main(args=None):
    rclpy.init(args=args)
    item_subsriber = FarmerItemSubscriber()
    rclpy.spin(item_subsriber)
    item_subsriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()