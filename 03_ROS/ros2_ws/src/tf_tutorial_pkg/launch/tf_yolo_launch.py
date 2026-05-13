from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition


def generate_launch_description():
    use_rviz_arg = DeclareLaunchArgument(
        'use_rviz',
        default_value='false',
        description='Launch RViz2 for visualization',
    )

    return LaunchDescription([
        use_rviz_arg,

        # Camera image publisher
        Node(package='camera_pkg', executable='img_pub'),

        # YOLO inference publisher
        Node(package='camera_pkg', executable='yolo_pub'),

        # Static TF: map → odom
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['2.0', '0.0', '0.0', '0', '0', '0', 'map', 'odom'],
        ),

        # Dynamic TF: odom → base_link
        Node(package='tf_tutorial_pkg', executable='odom_sim'),

        # Static TF: base_link → camera_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.1', '0.0', '0.2', '0', '0', '0', 'base_link', 'camera_link'],
        ),

        # Dynamic TF: YOLO object frame
        Node(package='tf_tutorial_pkg', executable='tf_yolo'),

        # TF listener
        Node(package='tf_tutorial_pkg', executable='tf_listener'),

        # RViz2 (optional)
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', '~/tf_tutorial.rviz'],
            condition=IfCondition(LaunchConfiguration('use_rviz')),
        ),
    ])
