import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64MultiArray

import math

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('my_sub_pub')
        self.subscription = self.create_subscription(
            Vector3, 'my_point_topic', self.listener_callback,10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(Float64MultiArray, 'my_polar_topic', 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%f %f %f"' % (msg.x, msg.y, msg.z))

        rdist = math.sqrt(msg.x**2.0 + msg.y**2)
        theta_rad = math.atan2(msg.y/rdist, msg.x/rdist)

        out_msg = Float64MultiArray()
        out_msg.data = [rdist, theta_rad]
        self.publisher.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()