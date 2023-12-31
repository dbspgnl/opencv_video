# SeamlessClone을 활용한 이미지 합성 (seamlessclone.py)

import cv2
import numpy as np
import matplotlib.pylab as plt

#--① 합성 대상 영상 읽기
# img1 = cv2.imread("data/01.mia_result_red1.png")
img1 = cv2.imread("data/01.mia.JPG")
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1 = cv2.resize(img1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
img2= cv2.imread("data/4.png")

#--② 마스크 생성, 합성할 이미지 전체 영역을 255로 셋팅
mask = np.full_like(img1, 255)
# cv2.imshow('img1', img1)
# cv2.imshow('mask', mask)

#--③ 합성 대상 좌표 계산(img2의 중앙)
height, width = img2.shape[:2]
center = (width//2, height//2)

#--④ seamlessClone 으로 합성 
normal = cv2.seamlessClone(img1, img2, mask, center, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, center, cv2.MIXED_CLONE)

#--⑤ 결과 출력
cv2.imshow('normal', normal)
cv2.imshow('mixed', mixed)
cv2.waitKey()
cv2.destroyAllWindows()