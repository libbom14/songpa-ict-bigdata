###
# print("\t\t\t ** 구 구 단 ** ")
# for i in range(1,10,1):         # outer (외부 for, 행)
#     for j in range(2,10,1):     # innter (내부 for, 열)
#         print(f"{j} x {i} = {i*j}", end="\t")
#     print()
###

# ==============================================

###
# 중첩 반복문을 이용하여 출력1
# 1
# 22
# 333
# 4444
# 55555
###
# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print(i, end="")
#     print()

# ==============================================

###
# 중첩 반복문을 이용하여 출력2
# 1
# 12
# 123
# 1234
# 12345
###
# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         print(j, end="")
#     print()

# ==============================================

###
# 중첩 반복문을 이용하여 출력3
# 54321
# 5432
# 543
# 54
# 5
###
# for i in range(5):
#     for j in range(5, i, -1):
#         print(j, end="")
#     print()

# ==============================================

###
# 중첩 반복문을 이용하여 출력4
# 5
# 54
# 543
# 5432
# 54321
###
# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end="")
#     print()

# ==============================================

###
# 중첩 반복문을 이용하여 출력5
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
###
# cnt = 0
# for i in range(1, 6, 1):
#     for j in range(1, i + 1, 1):
#         cnt += 1
#         print(cnt, end=" ")
#     print()

# ==============================================

###
# 중첩 반복문을 이용하여 출력6
# 1
# 23
# 345
# 4567
# 56789
###
cnt = 0
for i in range(1, 6, 1):
    cnt = i - 1
    for j in range(1, i + 1, 1):
        cnt += 1
        print(cnt, end=" ")
    print()
