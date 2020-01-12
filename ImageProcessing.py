#cv2.imread(file_name, flag) : 이미지를 읽어 Numpy 객체로 만드는 함수
#flag 종류
#IMREAD_COLOR : 이미지를 Color로 읽고, 투명한 부분은 무시
#IMREAD_GRAYSCALE : 이미지를  Grayscale로 읽기
#IMREAD_UNCHANGED : 이미지를 Color로 읽고, 투명한 부분도 읽기(Alpha)
#반환값 : Numpy 객체(행, 열, 색상 : 기본 BGR)

#cv2.imshow(title. image) : 특정한 이미지를 화면에 출력

#cv2.imwrite(file_name, image) : 특정한 이미지를 파일로 저장하는 함수

#cv2.waitKey(time) : 키보드 입력을 처리하는 함수, time = 0이면 무한대기(키입력까지)
#반환값 : 입력한 값의 아스키코드

#cv2.destroyAllWindows() : 열려있는 윈도우창 다 닫기

import cv2
img_basic = cv2.imread('dog.png', cv2.IMREAD_COLOR)
cv2.imshow('Image_basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png', img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image_gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)

