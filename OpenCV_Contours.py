#cv2.findContours(image, mode, method) : 이미지에서 외곽을 찾는 함수
#이미지는 Gray Scale Threshold 전처리 과정이 필요
#cv2.drawContours(image, contours, contour_index, color, thickness)

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('stairs.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1] # [1] 안붙이면 오류뜸
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()