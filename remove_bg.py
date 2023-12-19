import cv2

image = cv2.imread('custom/save/01.mia_result_red1.png')
img_origin = image
# image = 255 - image

# 전처리
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 블러 처리
# blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
# cv2.imshow('blurred_image', blurred_image)

# 임계값 설정
_, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV)
thresholded_image = 255 - thresholded_image
cv2.imshow('thresholded_image', thresholded_image)

# 배경 제거
r, g, b = cv2.split(img_origin)
rgba = [r,g,b,thresholded_image]
dst = cv2.merge(rgba,4)
cv2.imshow('dst', dst)

# Thresholding을 이용하여 이미지에 적용
# image_no_background = cv2.bitwise_and(image, image, mask=thresholded_image)
# cv2.imshow('No Background Image', image_no_background)

cv2.waitKey(0)
cv2.imwrite('custom/result.png', dst)