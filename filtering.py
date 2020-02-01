#컨볼루션 계산(각 자리끼리 계산)
#필터링에서 컨볼루션은 smoothing처리를 하는 것이라고 보면됨.
#가중치를 곱해서 계산해준 뒤 가중치의 합으로 나누어줌
#basic Kernel(전부 같은 가중치를 가짐) , Gaussian Kernel(정규 분포처럼 중앙에 높은값, 바깥으로 갈수록 작은 가중치값)

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('result2.png')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

dst = cv2.filter2D(image, -1, kernel)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()

#내장함수 blur
#dst = cv2.blur(image, (4,4)) 하면 위의 결과와 같은 출력 나옴

#가우시안 blur은 커널의 크기가 홀수가 되어야함.
#dst = cv2.GaussianBlur(image, (5,5), 0)

#사이즈가 커지면 커질수록 좀 더 뿌얘짐