import cv2
import numpy as np

def nothing(x):
    pass

def ImageBlending():
    
    video1 = cv2.VideoCapture('custom/1m.mp4')
    video2 = cv2.VideoCapture('custom/cox_output.mp4')
    width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output = cv2.VideoWriter('custom/cox_final_output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
    
    # cv2.namedWindow("ImageP")
    # cv2.createTrackbar('Mixing', 'ImageP', 0,100 , nothing)
    # mix = cv2.getTrackbarPos('Mixing','ImageP')

    while True:

        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()
        if not ret1:
            break

        # mix = cv2.getTrackbarPos("Mixing","ImageP")
        # result = cv2.addWeighted(frame1, float(100-mix)/100, frame2, float(mix)/100, 0)
        result = cv2.addWeighted(frame1, 0.4, frame2, 0.6, 0)

        cv2.imshow("ImageP",result)
        output.write(result) # 파일

        k = cv2.waitKey(1)
        if k == 27:
            break

    cv2.destroyAllWindows()
    
ImageBlending()