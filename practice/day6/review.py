###
# 5. 중첩 반복문을 활용해서 숫자 삼각형을 출력해보세요.
#      1
#     12
#    123
#   1234
#  12345 ###

# for i in range(1, 6):
#     # print(" "*(5-i), end="")
#     for k in range(5 - i, 0, -1):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(f"{j}", end="")
#     print()

###
# 6. num=[15,23,47,58,11] 리스트에서 가장 큰 값을 출력하는 함수 프로그램을 작성해보세요.
# 6-1. list와 for 반복문을 이용해서 문제 해결
# 6-2. 함수를 이용해서 문제 해결
# ###

numbers = [15, 23, 47, 58, 11]
result = numbers[0]
for number in numbers:
    if result < number:
        result = number
print(f"최대값1 = {result}")


# ==================================

def get_max(numlist):
    max_num = numlist[0]
    for num in numlist:
        if max_num < num:
            max_num = num
    print(f"최대값2 = {result}")


get_max(numbers)


# ==================================

def maxNum(n):
    max_num = n[0]
    for i in n:
        if i > max_num:
            max_num = i
    return max_num


print("최대값3 = {}".format(maxNum(numbers)))

# ==================================
