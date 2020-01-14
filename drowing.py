#직선 그리기
#cv2.line(image_start, start, end, color, thickness)
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8) #uint8 : 양수만 표현하는 int, 8은 2^8개의 표현가능한 수
image = cv2.line(image, (0,0), (255, 255), (255, 0, 0), 3)
plt.imshow(image)
plt.show()

#사각형 그리기
#cv2.rectangle(image, start, end, color, thickness)
image = np.full((512, 512, 3), 255, np.uint8)
image1 = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 10)
plt.imshow(image1)
plt.show()

#원 그리기
#cv2.circle(image, center, radian(반지름), color, thickness)
image = np.full((512, 512, 3), 255, np.uint8)
image2 = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)
plt.imshow(image2)
plt.show()

#다각형 그리기
#cv2.polylines(image, points, is_closed, color, thickness)
image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5,5], [128,258], [483, 444], [400, 150]])
image3 = cv2.polylines(image, [points], True, (0, 0, 255), 4)
plt.imshow(image3)
plt.show()
