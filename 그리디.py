import cv2

cap = cv2.VideoCapture(0)      # 동영상 캡처 객체 생성
if cap.isOpened():                      # 캡처 객체 초기화 확인
    while True: 
        ret, img = cap.read()           # 다음 프레임 읽기
        if ret:                         # 프레임 읽기 정상
            cv2.imshow('cam',img) # 화면에 표시
            cv2.waitKey(25)             # 25ms 지연(40fps로 가정)
        else:                           # 다음 프레임을 읽을 수 없음.
            break
    
else:
    print("Can't open video.")          # 캡처 객체 초기화 실패
cap.release()                           # 캡쳐 자원 반납
cv2.destroyAllWindows()