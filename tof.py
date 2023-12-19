import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    depth_map = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 가장 가까운 객체 추출
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(depth_map)
    cv2.circle(frame, max_loc, 10, (0, 0, 255), -1)

    cv2.imshow('Object Tracking', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()