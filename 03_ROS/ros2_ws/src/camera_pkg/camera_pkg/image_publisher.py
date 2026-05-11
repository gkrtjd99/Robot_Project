import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from ultralytics import YOLO


class ImagePublisher(Node):
    def __init__(self):
        super().__init__("image_publisher")

        # Publish camera frames with YOLO detections to ROS2 topic.
        self.publisher_ = self.create_publisher(Image, "image_raw", 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz

        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()

        if not self.cap.isOpened():
            self.get_logger().error("웹캠(0번)을 열 수 없습니다.")

        # Load YOLOv8 model
        try:
            self.model = YOLO("yolov8n.pt")
            self.get_logger().info("YOLOv8 모델 로드 완료")
        except Exception as e:
            self.get_logger().error(f"YOLOv8 모델 로드 실패: {e}")
            self.model = None

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warning("프레임을 읽지 못했습니다.")
            return

        # Run YOLO detection
        if self.model is not None:
            results = self.model(frame, verbose=False)
            
            # Draw bounding boxes on frame
            for result in results:
                for box in result.boxes:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls_id = int(box.cls[0])
                    cls_name = result.names[cls_id]
                    
                    # Draw rectangle with label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    label = f"{cls_name} {conf:.2f}"
                    cv2.putText(frame, label, (x1, y1 - 10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        img_msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        img_msg.header.stamp = self.get_clock().now().to_msg()
        img_msg.header.frame_id = "camera_link"
        self.publisher_.publish(img_msg)

    def destroy_node(self):
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()