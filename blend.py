import cv2
import numpy as np

def nothing(x):
    pass

def ImageBlending():

    img1 = "data/4.png"
    img2 = "data/result.png"

    im1 = cv2.imread(img1)
    im1 = cv2.resize(im1, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    im2 = cv2.imread(img2)
    im2 = cv2.resize(im2, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    
    # 트랙바 생성전 윈도창 생성
    cv2.namedWindow("ImageP")
    # 생성된 윈도창에다가 Mixing 메뉴바를 가진 0~100 범위의 트랙바 생성
    cv2.createTrackbar('Mixing', 'ImageP', 0,100 , nothing)
    # 트랙바의 값을 mix 에 삽입 ( 초기값은 0이기 때문에 현재는 mix 값이 0 임 )
    mix = cv2.getTrackbarPos('Mixing','ImageP')

    while True:

        # 블렌딩 공식을 활용하여 mix값에 따라서 각 이미지가 차지하는 비율이 서로
        # 반비례하도록 설정
        img = cv2.addWeighted(im1, float(100-mix)/100, im2 , float(mix)/100, 0)

        cv2.imshow("ImageP",img)

        k = cv2.waitKey(1)
        if k == 27:
            break

        # 인식된 트랙바의 값을 mix에 삽입하여 상태에 반영    
        mix = cv2.getTrackbarPos("Mixing","ImageP")

    cv2.destroyAllWindows()

ImageBlending()