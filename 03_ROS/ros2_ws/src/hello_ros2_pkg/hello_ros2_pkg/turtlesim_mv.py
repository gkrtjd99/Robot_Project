import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SquareMover(Node):
    def __init__(self):
        super().__init__('square_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # 0.5초마다 실행
        self.step = 0

    def timer_callback(self):
        msg = Twist()
        if self.step < 4:       # 2초 직진
            msg.linear.x = 1.0
        else:                   # 1초 회전
            msg.angular.z = 1.6
        self.publisher_.publish(msg)
        self.step = (self.step + 1) % 6  # 0~5 반복

def main(args=None):
    rclpy.init(args=args)
    node = SquareMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
