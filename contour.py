# import cv2

# src = cv2.imread("1.png", cv2.IMREAD_COLOR)

# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# binary = cv2.bitwise_not(binary)

# contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# for i in range(len(contours)):
#     cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
#     cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
#     print(i, hierarchy[0][i])
#     cv2.imshow("src", src)
#     cv2.waitKey(0)

# cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt

def pause():
    # pause
    keycode = cv2.waitKey(0)
    # ESC key to close imshow
    if keycode == 27:         
        cv2.destroyAllWindows()

w = 600
h = 800

# cv2.resize(img_bgr, (500, 500), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
img_bgr = cv2.imread('data/3.png')
cv2.namedWindow('img_bgr', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='img_bgr', width=w, height=h)
cv2.imshow("img_bgr", img_bgr)
pause()

img_bitwise_not_bgr = cv2.bitwise_not(img_bgr)
cv2.namedWindow('img_bitwise_not_bgr', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='img_bitwise_not_bgr', width=w, height=h)
cv2.imshow("img_bitwise_not_bgr", img_bitwise_not_bgr)
pause()

img_bitwise_not_bgr2gray = cv2.cvtColor(img_bitwise_not_bgr, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('img_bitwise_not_bgr2gray', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='img_bitwise_not_bgr2gray', width=w, height=h)
cv2.imshow("img_bitwise_not_bgr2gray", img_bitwise_not_bgr2gray)
pause()

ret, img_binary = cv2.threshold(img_bitwise_not_bgr2gray, 150,255,cv2.THRESH_BINARY)
cv2.namedWindow('img_binary', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='img_binary', width=w, height=h)
cv2.imshow("img_binary", img_binary)
pause()

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img_contour = cv2.drawContours(img_bgr, contours, -1, (0, 255, 0), 2)
cv2.namedWindow('img_contour', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='img_contour', width=w, height=h)
cv2.imshow("img_contour", img_contour)
pause()