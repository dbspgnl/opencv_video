import cv2

src = cv2.imread('data/01.mia_result_red.png')
src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
mask = cv2.imread('data/01.mia_result_0.5gray.png', cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, dsize=(640, 480), interpolation=cv2.INTER_AREA)
background = cv2.imread('data/4.png')
background = cv2.resize(background, dsize=(640, 480), interpolation=cv2.INTER_AREA)

# print(src)
tmp = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
r, g, b = cv2.split(src)
rgba = [r,g,b,alpha]
dst1 = cv2.merge(rgba,4)

mask = cv2.copyTo(src, mask, background)
# img = cv2.addWeighted(dst, 0.8, mask, 0.2, 0)
while True:
	cv2.imshow("alpha", dst1)
	cv2.imshow("mask", mask)
	# cv2.imshow("ImageP",img)
	k = cv2.waitKey(1)
	if k == 27:
		break