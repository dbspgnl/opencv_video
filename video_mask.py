import cv2
import math
import numpy as np

# 합성할 이미지와 동영상 로드
image = cv2.imread('data/01.mia_result_red1.png', cv2.IMREAD_UNCHANGED)
mask = cv2.imread('data/01.mia_result_gray.png', cv2.IMREAD_GRAYSCALE)
video = cv2.VideoCapture('data/40s.mp4')

# 동영상의 프레임 크기 조정
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
image = cv2.resize(image, (width, height))
mask = cv2.resize(mask, (width, height))

# 동영상 합성
output = cv2.VideoWriter('data/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

def FixImage(img, angle, scale, xAxis, yAxis):
    if img.ndim > 2:
        height, width, channel = img.shape
    else:
        height, width = img.shape
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, scale)
    result = cv2.warpAffine(img, matrix, (width, height))
    M = np.float32([[1,0,xAxis],[0,1,yAxis]]) # x,y
    result = cv2.warpAffine(result, M,(width, height))
    return result

def PrintPosition():
    print(f"x: {xAxis} / y: {yAxis} / rotate: {rotate} / scale: {scale}")

xAxis = -115
yAxis = 55
rotate = -715
rad = rotate * math.pi / 180
scale = 1.15

# desired_alpha = 30
# alpha = desired_alpha / 255.0

while True:
    
	# 비디오 읽기
    ret, frame = video.read()

    if not ret:
        break
    
    # 키보드 동작
    keyboard = cv2.waitKey(30)
    if keyboard == ord('q'): # 좌회전
        rotate += 5
        rad = rotate * math.pi / 180
        PrintPosition()
    elif keyboard == ord('e'): # 우회전
        rotate -= 5
        rad = rotate * math.pi / 180
        PrintPosition()
    elif keyboard == ord('w'): # 상
        yAxis -= 5
        PrintPosition()
    elif keyboard == ord('s'): # 하
        yAxis += 5
        PrintPosition()
    elif keyboard == ord('a'): # 좌
        xAxis -= 5
        PrintPosition()
    elif keyboard == ord('d'): # 우
        xAxis += 5
        PrintPosition()
    elif keyboard == ord('c'): # 대
        scale += 0.025
        PrintPosition()
    elif keyboard == ord('z'): # 소
        scale -= 0.025
        PrintPosition()
    elif keyboard == 27: # ESC
        break

    fixed_img = FixImage(image, rad, scale, xAxis, yAxis)
    fixed_mask = FixImage(mask, rad, scale, xAxis, yAxis)
    # frame = cv2.addWeighted(frame, 0.7, result, 0.3, 0)
    # frame = cv2.addWeighted(frame, 1, fixed_img, alpha, 0)
    frame = cv2.copyTo(fixed_img, fixed_mask, frame)
    cv2.imshow("viewer", frame)     
    output.write(frame) # 파일
    
# 사용한 리소스 해제
video.release()
output.release()