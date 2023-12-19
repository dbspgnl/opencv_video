import cv2
import math
import numpy as np

# 합성할 이미지와 동영상 로드
image = cv2.imread('custom/save/01.mia_result_red1.png', cv2.IMREAD_UNCHANGED)
# image = cv2.imread('custom/result.png', c)
mask = cv2.imread('custom/save/01.mia_result_gray.png', cv2.IMREAD_GRAYSCALE)
video = cv2.VideoCapture('custom/40s.mp4')
video_origin = video
fps = 30

# 동영상의 프레임 크기 조정
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
image = cv2.resize(image, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
mask = cv2.resize(mask, dsize=(width, height), interpolation=cv2.INTER_LINEAR)

# 동영상 합성
output = cv2.VideoWriter('data/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

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
    print(f"x: {xAxis} / y: {yAxis} / rotate: {rotate} / scale: {scale} / mix: {mix}")

xAxis = 125
yAxis = -35
rotate = 137
rad = rotate * math.pi / 180
scale = 1.645
mix = 30

delay = round(1000/fps)

while True:
    
	# 비디오 읽기
    ret, frame = video.read()
    _, origin_frame = video_origin.read()
    
    if not ret:
        break
    
    # 키보드 동작
    keyboard = cv2.waitKey(delay)
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
    elif keyboard == ord('f'): # 옅게
        mix -= 5
        PrintPosition()
    elif keyboard == ord('g'): # 진하게
        mix += 5
        PrintPosition()
    elif keyboard == 27: # ESC
        break

    # 도면 합성
    fixed_img = FixImage(image, rad, scale, xAxis, yAxis)
    fixed_mask = FixImage(mask, rad, scale, xAxis, yAxis)
    fixed = cv2.copyTo(fixed_img, fixed_mask, frame)
    # result = frame * fixed_img
    
    # 원본 영상과 블렌딩
    result = cv2.addWeighted(origin_frame, float(100-mix)/100, fixed, float(mix)/100, 0)
    cv2.imshow("viewer", result)     
    # output.write(result) # 파일
    
    
    
# 사용한 리소스 해제
video.release()
output.release()