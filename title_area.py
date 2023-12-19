# 영상 위에 영역과 타이틀 라벨 처리 합성
import cv2
import numpy as np
from numpy import random
from PIL import ImageFont, ImageDraw, Image
    
title_area = [[(200, 510), (330, 545)], [(680, 490), (770, 525)], [(1450, 520), (1590, 560)]]
title_text = ["대기행렬, 밀도", "상충", "속도"]

def main():
    video = cv2.VideoCapture('data/js_02_10s.mp4')
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    output = cv2.VideoWriter('custom/label_output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    color = [random.randint(0, 255) for _ in range(3)] # 컬러링
    title_bg = (50,80,240)

    while True:
        ret, frame = video.read()        
        if not ret:
            break
        
        # 영역
        # cv2.rectangle(frame, (12, 621), (564, 697), title_bg)
        points1 = np.array([[50, 625],[568, 600],[564, 690],[50, 710]], np.int32)
        frame = cv2.polylines(frame, [points1], True, title_bg, 2)
        cv2.rectangle(frame, (636, 576), (788, 720), title_bg, 2)
        cv2.rectangle(frame, (1399, 605), (1571, 649), title_bg, 2)
        
        # # 타이틀 배경
        # cv2.rectangle(frame, title_area[0][0], title_area[0][1], title_bg, -1, cv2.LINE_AA)
        # cv2.rectangle(frame, title_area[1][0], title_area[1][1], title_bg, -1, cv2.LINE_AA)
        # cv2.rectangle(frame, title_area[2][0], title_area[2][1], title_bg, -1, cv2.LINE_AA)
        
        # fil로 변환 (한글 처리)
        frame = Image.fromarray(frame)
        draw = ImageDraw.Draw(frame)
        font=ImageFont.truetype("data/NotoSansKR-Black.ttf",50)
        font1=ImageFont.truetype("data/NotoSansKR-Black.ttf",51)
        font2=ImageFont.truetype("data/NotoSansKR-Black.ttf",52)

        draw.text(title_area[0][0], title_text[0],font=font1,fill=(0,0,0))
        draw.text(title_area[0][0], title_text[0],font=font,fill=(255,255,255))
        draw.text(title_area[1][0], title_text[1],font=font2,fill=(0,0,0))
        draw.text(title_area[1][0], title_text[1],font=font,fill=(255,255,255))
        draw.text(title_area[2][0], title_text[2],font=font2,fill=(0,0,0))
        draw.text(title_area[2][0], title_text[2],font=font,fill=(255,255,255))
        
        
        frame = np.array(frame) # 다시 np 배열로
        
        cv2.imshow('Object Tracking', frame)
        
        output.write(frame) # 파일

        if cv2.waitKey(1) == 27: # ESC 종료
            break
        if cv2.waitKey(1) == 32: # 스페이스 일시정지
            while True:
                if cv2.waitKey(1) == 32:
                    break

    # cap.release()
    cv2.destroyAllWindows()

main()