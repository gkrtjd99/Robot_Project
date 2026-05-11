import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger


class ImageProcessor(Node):
    def __init__(self):
        super().__init__("image_processor")

        self.bridge = CvBridge()
        self.current_frame = None

        # Create subscription to receive images from image_publisher.
        self.subscription = self.create_subscription(
            Image, "image_raw", self.image_callback, 10
        )

        # Create publisher for Canny edge detection results.
        self.edge_publisher = self.create_publisher(Image, "image_edge", 10)

        # Create service to capture snapshot on demand.
        self.srv = self.create_service(
            Trigger, "capture_snapshot", self.capture_callback
        )

        self.get_logger().info("ImageProcessor node started.")

    def image_callback(self, msg):
        # Convert ROS2 Image message to OpenCV format.
        self.current_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        cv2.imshow("Camera View", self.current_frame)

        # Apply Canny edge detection and publish to /image_edge topic.
        gray = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, 100, 200)
        
        # Display edge detection result
        cv2.imshow("Edge Detection", edge)
        cv2.waitKey(1)
        
        edge_msg = self.bridge.cv2_to_imgmsg(edge, encoding="mono8")
        edge_msg.header.stamp = msg.header.stamp
        edge_msg.header.frame_id = msg.header.frame_id
        self.edge_publisher.publish(edge_msg)

    def capture_callback(self, request, response):
        if self.current_frame is not None:
            cv2.imwrite("snapshot.jpg", self.current_frame)
            response.success = True
            response.message = "snapshot.jpg로 저장되었습니다!"
            self.get_logger().info("Snapshot captured: snapshot.jpg")
        else:
            response.success = False
            response.message = "이미지가 아직 수신되지 않았습니다."
            self.get_logger().warning("No frame received yet.")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
