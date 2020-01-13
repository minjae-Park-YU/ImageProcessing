import cv2
image = cv2.imread('cat.jpg')

#픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

#이미지 Numpy 객체의 특정 픽셀을 가리킴
px = image[100, 100]

#B, G, R 순서로 출력된다.
#Grayscale일때는 구분 X
print(px)

#R값만 출력하기
print(px[2])

#특정 범위 픽셀 변경
image[0:100, 0:100] = [0, 0, 0] #반복문 돌리는 것 보다 범위 지정해서 한번에 바꾸는게 빠름

#ROI(Region of interesting - 목표 대상이 속하는 부분, 유의미한 부분) 추출 및 복사
roi = image[200:350, 50:200]
image[0:150, 0:150] = roi #이렇게하면 복사 붙여넣기 됨

#픽셀별로 색상 다루기(빨간색 없애기)
image[:, :, 2] = 0
