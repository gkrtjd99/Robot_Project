import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.declare_parameter('vel_x', 1.0)
        self.declare_parameter('angle_z', math.pi / 2)
        self.vel_x = self.get_parameter('vel_x').value
        self.angle_z = self.get_parameter('angle_z').value
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.step = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        if self.step % 2 == 0:
            msg.linear.x = self.vel_x
        else:
            msg.angular.z = self.angle_z
        self.pub.publish(msg)
        self.step += 1  
        if self.step >= 8:
            self.step = 0
            self.get_logger().info('Completed one square!')
        
def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TurtleSquare())