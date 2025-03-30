import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess

def generate_launch_description():
    config = os.path.join(get_package_share_directory('takeout3week'), 'config', 'roi.yaml')
    rviz_config_file = os.path.join(
        get_package_share_directory('takeout3week'), 'config', 'roi.rviz'
    )
    
    rosbag_file = os.path.join(
        get_package_share_directory('takeout3week'), 'bag', 'bag1.db3'
    )

    return LaunchDescription([

        Node(
            package='takeout3week',
            executable='pointcloud_roi',
            name='pointcloud_roi',
            parameters=[config]
        ),

        # RViz 실행
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        ),
        
        # ROS 2 bag 재생
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', rosbag_file],
            output='screen'
        )
    ])
