import numpy as np

#단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')

#복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']

#Numpy 원소 오름차순 정렬
array3 = np.array([5, 9, 10, 3, 1])
array3.sort()

#내림차순 정렬
print(array[::-1])

#각 열을 기준으로 정렬(오름차순)
array4 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
array4.sort()

#균일한 간격으로 데이터 생성
array5 = np.linspace(0, 10, 5)

#난수의 재연(실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2,3)))

#Numpy 배열 객체 복사
array6 = np.arange(0, 10)
array7 = array6
array7[0] = 99 #포인터처럼 원래 값도 바뀜
array7 = array6.copy() #이거쓰면 복사라서 괜춘

#중복된 원소 제거
array8 = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array8))
