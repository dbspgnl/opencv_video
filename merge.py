# 투명 배경 PNG 파일을 이용한 합성 (addition_rgba_mask.py)

import cv2
import numpy as np

#--① 합성에 사용할 영상 읽기, 전경 영상은 4채널 png 파일
img_fg = cv2.imread('data/pin.png', cv2.IMREAD_UNCHANGED)
img_fg = cv2.resize(img_fg, dsize=(640, 480), interpolation=cv2.INTER_AREA)
img_bg = cv2.imread('data/4.png')
back = img_bg
back = cv2.resize(back, dsize=(640, 480), interpolation=cv2.INTER_AREA)

#--② 알파채널을 이용해서 마스크와 역마스크 생성
_, mask = cv2.threshold(img_fg[:,:,3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#--③ 전경 영상 크기로 배경 영상에서 ROI 잘라내기
img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)
h, w = img_fg.shape[:2]
roi = img_bg[10:10+h, 10:10+w ]

#--④ 마스크 이용해서 오려내기
masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask)
masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# back = cv2.bitwise_and(img_bg, img_bg, mask=mask_inv)

#--⑥ 이미지 합성
added = masked_fg + masked_bg
img_bg[10:10+h, 10:10+w] = added

# cv2.imshow('mask', mask)
# cv2.imshow('mask_inv', mask_inv)
# cv2.imshow('masked_fg', masked_fg)
# cv2.imshow('masked_bg', masked_bg)
# cv2.imshow('added', added)
# cv2.imshow('result', img_bg)


cv2.namedWindow("blending") 
cv2.createTrackbar('Mixing', 'blending', 0,100, lambda x:x) 
mix = cv2.getTrackbarPos('Mixing','blending')
while True:
    # 트랙바
    blending = cv2.addWeighted(back, float(100-mix)/100, added , float(mix)/100, 0)
    cv2.imshow('blending', blending)

    mix = cv2.getTrackbarPos('Mixing','blending')
    k = cv2.waitKey(1)
    if k == 27:
        break

# 종료
cv2.waitKey()
cv2.destroyAllWindows()