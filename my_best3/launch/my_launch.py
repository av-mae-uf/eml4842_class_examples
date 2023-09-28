from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

config_dir = get_package_share_directory("my_best3")

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_best3',
            executable='pub_me',
            name='my_pub',
            parameters = [
                {'A1': 23.3},
                {'A2': 5.5}
            ],
            output='screen'
        ),
        Node(
            package='my_best3',
            executable='lets_go',
            name='my_sub_pub', 
            output='screen'
        ),
    ])
