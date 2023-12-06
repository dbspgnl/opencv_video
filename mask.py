import cv2

src = cv2.imread('data/result.png')
src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
mask = cv2.imread('data/result.png', cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst = cv2.imread('data/4.png')
dst = cv2.resize(dst, dsize=(640, 480), interpolation=cv2.INTER_AREA)

img = cv2.copyTo(src, mask, dst)
while True:
	cv2.imshow("ImageP",img)
	k = cv2.waitKey(1)
	if k == 27:
		break