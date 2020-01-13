import cv2
import numpy as np
import matplotlib.pyplot as plt

#이미지 크기 조절(인터폴레이션)
#cv2.resize(image, dsize, fx, fy, interpolation) / IMTER_CUBIC(사이즈크게할때), INTER_AREA(사이즈 작게할떄)
image = cv2.imread('cat.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #matplotlib에서는 RGB순서대로 처리
plt.show()

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show()

#이미지 위치 변경
#cv2.warpAffine(image, M, dsize)/ M : 변환행렬, disze : 매뉴얼 사이즈
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()

#이미지 회전
#cv2.getRotationMatrix2D(center, angle, scale)
M = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()

