import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class OperationOutputSubscriber(Node):
    
    def __init__(self):
        super().__init__("output_displayer")
        self.display_add = self.create_subscription(Int64,"/output/addition",self.add_disp_callback,10)
        self.display_sub = self.create_subscription(Int64,"/output/subtraction",self.sub_disp_callback,10)
        self.display_mul = self.create_subscription(Int64,"/output/multiplication",self.mul_disp_callback,10)
        self.display_div = self.create_subscription(Int64,"/output/division",self.div_disp_callback,10)

    def add_disp_callback(self, msg):
        self.get_logger().info("The output of addition is: " + str(msg.data))

    def sub_disp_callback(self, msg):
        self.get_logger().info("The output of subtraction is: " + str(msg.data))
    
    def mul_disp_callback(self, msg):
        self.get_logger().info("The output of multiplication is: " + str(msg.data))
    
    def div_disp_callback(self, msg):
        self.get_logger().info("The output of division is: " + str(msg.data))

def main(args=None):
    rclpy.init(args=args)
    output_display = OperationOutputSubscriber()
    rclpy.spin(output_display)
    output_display.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()