import cv2
import matplotlib.pyplot as plt

image_1 = cv2.imread('image1.jpg')
image_2 = cv2.imread('image2.jpg')
result = cv2.add(image_1, image_2)

#세터레이션 합(좀 더 자연스러움)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

#넘파이 합
result = image_1 + image_2
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

#임계점 처리하기(쓰레시홀드)
#cv2.threshold(image, thresh, max_value, type) : 입계값을 기준으로 훅백으로 분류하는 함수
image = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)

images = [] #이미지 모아놓을 리스트
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i,cv2.COLOR_GRAY2RGB))
    plt.show()

#적응 임계점 처리(여러개의 필터를 이용하여 부분마다 필터처리)
#cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C)

image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres1, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2, cv2.COLOR_GRAY2RGB))
plt.show()