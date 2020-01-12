import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

#스칼라 위치별 곱셈
multi_array = array * 10
print(multi_array)

#크기가 다른 배열의 합
#브로드캐스팅 : 크기에 맞게 자동으로 배열 확장
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2) #1X2 행렬이 2X2 행렬로 브로드캐스팅
array3 = array1 + array2
print(array3)

array4 = np.arange(0, 8).reshape(2, 4)
array5 = np.arange(0, 8).reshape(2, 4)
array6 = np.concatenate([array4, array5], axis=0)
array7 = np.arange(0, 4).reshape(4, 1)
print(array6 + array7)

#마스킹 연산 : 각 원소에 대해 조건에 맞는지 체크
array8 = np.arange(16).reshape(4, 4)
array9 = array8 < 10
print(array9)
array8[array9] = 100 #True로 판명된 원소들을 100으로 교체
print(array8)

#집계 함수(최대, 평균, 최소 등)
array10 = np.arange(16).reshape(4, 4)
print("최대값 : ", np.max(array10))
print("최소값 : ", np.min(array10))
print("합계 : ", np.sum(array10))
print("평균값 : ", np.mean(array10))

#행, 열별로 집계함수 구하기
print("열별 합계 : ", np.sum(array10, axis=0))