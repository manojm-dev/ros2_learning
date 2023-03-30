import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64,Int64MultiArray

class PublishOperands(Node):

    def __init__(self):
        super().__init__("operand_publisher")
        self.publisher_add = self.create_publisher(Int64MultiArray,"/operands/addition",10)
        self.publisher_sub = self.create_publisher(Int64MultiArray,"/operands/subtraction",10)
        self.publisher_mul = self.create_publisher(Int64MultiArray,"/operands/multiplication",10)
        self.publisher_div = self.create_publisher(Int64MultiArray,"/operands/division",10)
        self.count = 0
        self.create_timer(1.0,self.publish_callback)

    def publish_callback(self):

        #declaring types
        operand1 = operand2 = Int64()

        #assigning value
        operand1.data = operand2.data = self.count

        #creating a int64 type multiarray to store the both operands
        msg = Int64MultiArray()

        #assinging the array in multiarray
        msg.data = [operand1.data,operand2.data]

        #publishing the operands
        self.publisher_add.publish(msg)
        self.publisher_sub.publish(msg)
        self.publisher_mul.publish(msg)
        self.publisher_div.publish(msg)

        #logging that we have published
        self.get_logger().info("The operands are published")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    publish_operands = PublishOperands()
    rclpy.spin(publish_operands)
    publish_operands.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
