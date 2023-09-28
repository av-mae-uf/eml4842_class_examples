# Node:
# Written by:
# Date Created: Jan 2023
# Description: Python ROS2 node for converting joystick commands to msgs to send to the controller.

# Import all Necessary Python Modules Here

import math

# Import all Necessary ROS2 Modules Here, this includes messages (std_msgs.msg for Int16, geometry_msgs.msg for Pose) Look at this
# for all message data: https://av1tenth-docs.readthedocs.io/en/latest/information/ros2_common_msgs.html

import rclpy
from rclpy.node import Node
from rclpy.clock import Clock
from std_msgs.msg import Int16, Float32, String
from geometry_msgs.msg import Vector3

from av_interfaces.srv import Distance


class NodeTemplate(Node):
    """Node Description"""

    def __init__(self):
        super().__init__("my_pub")

        self.publisher = self.create_publisher(msg_type = Vector3, topic = 'my_point_topic', qos_profile = 1)
        self.timer = self.create_timer(timer_period_sec = 0.5 , callback = self.my_timer_function)

        self.declare_parameter('A1', 5.0)
        self.declare_parameter('A2', 8.0)

        self.start_time = Clock().now().nanoseconds # this will store the initial time value
        self.elapsed_time = 0

        self.total_dist_traveled = 0.0
        self.last_x = 0.0
        self.last_y = 0.0
        self.first_time = True

        self.srv = self.create_service(Distance, 'distance_traveled', self.reply_to_client)

    def reply_to_client(self, request, response):
        self.get_logger().info(f'Incoming request from {request.name}')
        response.dist = self.total_dist_traveled
        return response

    def my_timer_function(self):
        """Description of Callback"""
        self.elapsed_time = Clock().now().nanoseconds - self.start_time
        elapsed_time_sec = self.elapsed_time / 1.0E9

        A1 = self.get_parameter('A1').value
        A2 = self.get_parameter('A2').value

        msg = Vector3()
        msg.x = A1 * math.cos(0.2*elapsed_time_sec + math.pi/2.0)
        msg.y = A2 * math.sin(0.6*elapsed_time_sec)
        msg.z =  0.0
        self.publisher.publish(msg)

        self.get_logger().info(f"A1 = {A1}, A2 = {A2}, x and y = {msg.x} , {msg.y} total_dist = {self.total_dist_traveled}")
        
        if(self.first_time):
            self.last_x = msg.x
            self.last_y = msg.y
            self.first_time = False
        else:
            new_dist = math.sqrt((msg.x-self.last_x)**2 + (msg.y-self.last_y)**2)
            self.total_dist_traveled += new_dist
            self.last_x = msg.x
            self.last_y = msg.y

def main(args=None):
    rclpy.init(args=args)
    node_template = NodeTemplate()
    rclpy.spin(node_template)
    node_template.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
