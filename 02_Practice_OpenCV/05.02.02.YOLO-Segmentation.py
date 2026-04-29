from ultralytics import YOLO
import cv2

# COLORS = [
#     (255,  56,  56), (255, 157,  51), ( 81, 200, 120),
#     ( 51, 153, 255), (174,  60, 229), (255,  51, 153),
#     (255, 255,  51), ( 51, 255, 255), (153, 255,  51),
# ]

# COCO 17개 키포인트 연결 쌍 (스켈레톤)
SKELETON = [
    (0, 1), (0, 2), (1, 3), (2, 4),          # 얼굴
    (5, 6),                                    # 어깨
    (5, 7), (7, 9), (6, 8), (8, 10),          # 팔
    (5, 11), (6, 12), (11, 12),               # 몸통
    (11, 13), (13, 15), (12, 14), (14, 16),   # 다리
]

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    result = results[0]
    overlay = frame.copy()

    if result.keypoints is not None:
        kpts = result.keypoints.data  # (N, 17, 3) — x, y, conf

        for person in kpts:
            # 관절 점 그리기
            for x, y, conf in person:
                if conf > 0.5:
                    cv2.circle(overlay, (int(x), int(y)), 4, (0, 255, 0), -1)

            # 뼈대 연결선 그리기
            for a, b in SKELETON:
                xa, ya, ca = person[a]
                xb, yb, cb = person[b]
                if ca > 0.5 and cb > 0.5:
                    cv2.line(overlay, (int(xa), int(ya)), (int(xb), int(yb)),
                             (255, 100, 0), 2)

    cv2.imshow("YOLOv8 Pose Skeleton", overlay)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
