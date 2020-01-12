list_data = [1, 2, 3]
print(list_data) #기존의 리스트 사용방법

import numpy as np #넘파이 불러오기

array = np.array(list_data) #넘파이 데이터로 변경

print(array.size) #넘파이 크기
print(array.dtype) #넘파이 형식
print(array[2]) #넘파이 인덱스 접근

#0~3 까지의 배열 만들기
array1 = np.arange(4) #0~ (4-1) 까지 배열 만들기
print(array1)

array2 = np.zeros((4, 4), dtype=float) #크기만큼 원하는 타입으로 0초기화된 배열
print(array2)

array3 = np.ones((3, 3), dtype=str) #문자열도 가능. 1로 초기화
print(array3)

array4 = np.random.randint(0, 10, (3,3)) #0~9까지 랜덤한 정수로 3X3 행렬 만듬
print(array4)

#표준정규분포를 따르는 배열 만들기
array5 = np.random.normal(0, 1, (3,3))

#배열 합치기(가로)
array6 = np.array([1, 2, 3])
array7 = np.array([4, 5, 6])
array8 = np.concatenate([array6, array7]) #np.concatenate([]) : 배열 합치기
print(array8.shape)
print(array8)

#배열 크기 변경
array9 = np.array([1, 2, 3, 4])
array10 = array9.reshape((2, 2))
print(array10)

#배열 합치기(세로)
array11 = np.arange(4).reshape(1, 4)
array12 = np.arange(8).reshape(2, 4)
array13 = np.concatenate([array11, array12], axis = 0)
print(array13)

#배열 나누기
array14 = np.arange(8).reshape(2, 4)
left, right = np.split(array14, [2], axis=1)
print(left.shape)
print(right.shape)
print(array14)
print(left)


