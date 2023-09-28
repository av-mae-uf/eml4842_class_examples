
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, Float32, String
from av_interfaces.srv import Distance


class NodeTemplate(Node):
    """Node Description"""

    def __init__(self):
        super().__init__("my_client1")

        # self.subscription = self.create_subscription(msg_type = , topic = , callback = , qos_profile = 1)
        # self.publisher = self.create_publisher(msg_type = , topic = , qos_profile = 1)
        
        self.cli = self.create_client(Distance, 'distance_traveled')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Distance.Request() 
        
    def send_request(self, sendname):
        """Description of Callback"""
        self.get_logger().info('In the send request function.')
        self.req.name = sendname

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    node_template = NodeTemplate()
    response = node_template.send_request('Robert')

    node_template.get_logger().info(f'Distance travelled so far is {response.dist} meters.')

    node_template.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()