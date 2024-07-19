import numpy as np

num = [1, 2, 3]
num1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr1 = np.array(num)  # 배열로 변환

print(type(num1))
# <class 'list'>
print(type(arr1))
# <class 'numpy.ndarray'>

print(num1)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr1)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

for i in range(3):      # 3행
    for j in range(3):  # 3열
        print(num1[i][j], end="")
    print()

#  배열(행,열)의 길이를 자동으로 인식
for i in range(len(num1)):
    for j in range(len(num1[i])):
        print(num1[i][j], end=" ")
    print()

for i in range(len(arr1)):
    for j in range(arr1[i]):
        print(arr1[i][j], end=" ")
    print()

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)

arr1.shape