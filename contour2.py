import sys
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('line/20231208_173708.png', cv2.IMREAD_GRAYSCALE) # 그레이 스케일 영상

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150) # 하단 임계값과 상단 임계값은 실험적으로 결정하기
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
bgr = dst[:,:,0:3]
mask = cv2.inRange(bgr, (190,190,190), (255,255,255)) # bgr, gray, white
bgr_new = bgr.copy()
bgr_new[mask!=0] = (255,255,255) # white > White
# bgr_new[mask!=0] = (0,0,255) # white > RED
# bgr_new[mask!=255] = (0,0,255) # black > RED
result = bgr_new[:,:,0:3] # * 0.25 # 어둡게

# cv2.imshow('src', src)
cv2.imshow('dst', result)
cv2.waitKey()
cv2.imwrite('line/20231208_173708-alpha.png',result)

cv2.destroyAllWindows()