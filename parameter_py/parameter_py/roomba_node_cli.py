import rclpy
from rclpy.node import Node 

class PublishModeOfOperation(Node):
    
    def __init__(self):
        super().__init__("roomba")
        self.declare_parameter('roomba_mode','idle')
        self.create_timer(1.0,self.status_callback)

    def status_callback(self):
        roomba_mode = self.get_parameter('roomba_mode').get_parameter_value().string_value

        if roomba_mode == 'sweep':
            self.get_logger().info("Roomba is Sweeping..")
        elif roomba_mode == 'mop':
            self.get_logger().info("Roomba is Moping...")
        elif roomba_mode == 'idle':
            self.get_logger().info("Roomba is idle...")

    def set_mode(self, mode):
        allowed_modes = ['sweep', 'mop', 'idle']
        if mode in allowed_modes:
            self.get_logger().info("Setting Roomba mode to {}".format(mode))
            self.set_parameter('roomba_mode', mode)
        else:
            self.get_logger().warning("Invalid mode. Allowed modes are {}".format(allowed_modes))

def main(args=None):
    rclpy.init(args=args)
    roomba = PublishModeOfOperation()
    rclpy.spin(roomba)
    roomba.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
