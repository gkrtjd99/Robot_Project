import cv2
import numpy as np
from ultralytics import YOLO

def edge_detection_pipline():
    cap = cv2.VideoCapture(0)
    model = YOLO('yolov8n.pt')

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return
    while True:
        #프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break

        results = model. predict(frame, stream=True)

        for r in results:
            annotated_frame = r.plot()  # OpenCV
            cv2.imshow("YOLOv8 Real-time Inference", annotated_frame)

        #'q' 키를 누르면 종료 (25ms 대기)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    #리소스 해제
    cap.release()
    cv2.destroyAllWindows()

#실행
edge_detection_pipline()