import cv2       # OpenCV 라이브러리 임포트
import numpy as np  # 행렬 연산을 위한 NumPy

def edge_detection_pipeline():
    # 1. 웹캠 연결 (0번은 내장 웹캠)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return
    cv2.namedWindow('Controls')
    cv2.createTrackbar('Low Threshold', 'Controls', 100, 255, lambda x: None)
    cv2.createTrackbar('High Threshold', 'Controls', 200, 255, lambda x: None)
    
    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break
        # 2. 그레이스케일 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 3. 가우시안 블러 적용
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # 4. Canny 엣지 검출
        edges = cv2.Canny(blurred, 30, 90)
        
        low = cv2.getTrackbarPos('Low Threshold', 'Controls')
        high = cv2.getTrackbarPos('High Threshold', 'Controls')
        edges = cv2.Canny(blurred, low, high)

        # 5. 색상 필터링 (파란색 영역만 추출)
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # lower_blue = np.array([100, 150, 50])
        # upper_blue = np.array([140, 255, 255])
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # edges = cv2.bitwise_and(edges, edges, mask=mask)

        # 6. 키 입력 처리
        key = cv2.waitKey(25) & 0xFF
        if key == ord('s'):
            cv2.imwrite('result.png', edges)
            print("Image Saved!")
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # 결과 표시
        cv2.imshow('Original Video', frame)
        cv2.imshow('Edge Detection', edges)

        # 'q' 키를 누르면 종료 (25ms 대기)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # 리소스 해제
    cap.release()
    cv2.destroyAllWindows()

# 실행
edge_detection_pipeline()