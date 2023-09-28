import rclpy
from rclpy.node import Node
from rclpy.clock import Clock
import math

from geometry_msgs.msg import Vector3


class PointPublisher(Node):

    def __init__(self):
        super().__init__('my_pub')
        self.publisher_ = self.create_publisher(Vector3, 'my_point_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = Clock().now().nanoseconds
        self.elapsed_time = 0 # nanoseconds

        self.declare_parameter('A1', 5.0)
        self.declare_parameter('A2', 8.0)

    def timer_callback(self):

        self.elapsed_time = Clock().now().nanoseconds - self.start_time
        elapsed_time_seconds = self.elapsed_time / 1.0E9

        A1 = self.get_parameter('A1').value
        A2 = self.get_parameter('A2').value

        msg = Vector3()
        msg.x = A1 * math.cos(0.2*elapsed_time_seconds + math.pi/2.0)
        msg.y = A2 * math.sin(0.6*elapsed_time_seconds)
        msg.z = 0.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: %f %f %f %f %f' % (A1, A2, msg.x, msg.y, msg.z))
        
def main(args=None):
    rclpy.init(args=args)

    pt_publisher = PointPublisher()

    rclpy.spin(pt_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pt_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()