import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64,Int64MultiArray

class OperatorsPubSub(Node):

    def __init__(self):
        super().__init__("operator")
        
        #creating subscription for operands
        self.add_operand_sub = self.create_subscription(Int64MultiArray,"operands/addition",self.addition_callback,10)
        self.sub_operand_sub = self.create_subscription(Int64MultiArray,"operands/subtraction",self.subtraction_callback,10)
        self.mul_operand_sub= self.create_subscription(Int64MultiArray,"operands/multiplication",self.multiplication_callback,10)
        self.div_operand_sub = self.create_subscription(Int64MultiArray,"operands/division",self.division_callback,10)

        #creating publisher to publish the results
        self.add_publish = self.create_publisher(Int64,"output/addition",10)
        self.sub_publish = self.create_publisher(Int64,"output/subtraction",10)
        self.mul_publish = self.create_publisher(Int64,"output/multiplication",10)
        self.div_publish = self.create_publisher(Int64,"output/division",10)

    def addition_callback(self, msg:Int64MultiArray):
        operand1 = msg.data[0]
        operand2 = msg.data[1]
        output = operand1 + operand2
        output_msg = Int64()
        output_msg.data = int(output)
        self.add_publish.publish(output_msg)
        self.get_logger().info("The result of addition is published")
    
    def subtraction_callback(self, msg:Int64MultiArray):
        operand1 = msg.data[0]
        operand2 = msg.data[1]
        output = operand1 - operand2
        output_msg = Int64()
        output_msg.data = int(output)
        self.sub_publish.publish(output_msg)
        self.get_logger().info("The result of subtraction is published")

    def multiplication_callback(self, msg:Int64MultiArray):
        operand1 = msg.data[0]
        operand2 = msg.data[1]
        output = operand1 * operand2
        output_msg = Int64()
        output_msg.data = int(output)
        self.mul_publish.publish(output_msg)
        self.get_logger().info("The result of multiplication is published")

    def division_callback(self, msg:Int64MultiArray):
        operand1 = msg.data[0]
        operand2 = msg.data[1]
        
        #since anything/0 is undefined i am just assigning some data as output
        if (operand2>0):
            output = operand1 / operand2
        else:
            output = 0

        output_msg = Int64()
        output_msg.data = int(output)
        self.div_publish.publish(output_msg)
        self.get_logger().info("The result of division is published")


def main(args=None):
    rclpy.init(args=args)
    operators = OperatorsPubSub()
    rclpy.spin(operators)
    operators.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()