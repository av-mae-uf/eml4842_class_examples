# Node:
# Written by:
# Date Created: Jan 2023
# Description: Python ROS2 node for converting joystick commands to msgs to send to the controller.

# Import all Necessary Python Modules Here

# import something

# Import all Necessary ROS2 Modules Here, this includes messages (std_msgs.msg for Int16, geometry_msgs.msg for Pose) Look at this
# for all message data: https://av1tenth-docs.readthedocs.io/en/latest/information/ros2_common_msgs.html

import time
import rclpy

from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup

from rclpy.node import Node
from std_msgs.msg import Int16, Float32, String
from av_interfaces.srv import Distance


class CallbackGroupDemo(Node):
    """Node Description"""

    def __init__(self):
        super().__init__("my_client")

        # self.subscription = self.create_subscription(msg_type = , topic = , callback = , qos_profile = 1)
        # self.publisher = self.create_publisher(msg_type = , topic = , qos_profile = 1)
        
        client_cb_group = MutuallyExclusiveCallbackGroup()
        timer_cb_group = None
        self.client = self.create_client(Distance, 'distance_traveled', callback_group=client_cb_group)
        self.call_timer = self.create_timer(2, self.timer_callback, callback_group=timer_cb_group)

        self.req = Distance.Request() 
        
        
    def timer_callback(self):
        """Description of Callback"""
        self.get_logger().info('In the send request function.')
        self.req.name = 'Robert'

        self.response = self.client.call(self.req)
        self.get_logger().info(f'sent Robert')
        
        self.get_logger().info(f'It\'s been 2 seconds and dist so far = {self.response.dist}')
        
def main(args=None):
    rclpy.init()
    node = CallbackGroupDemo()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        node.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()