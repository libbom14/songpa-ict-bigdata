# 중첩 반복무을 사용하여 실행결과와 같이 숫자 삼각형을 출력
# [실행결과]
# 12345
#  2345
#   345
#    45
#     5

for i in range(5):
    print(" " * i, end="")
    for j in range(1 + i, 6, 1):
        print(j, end="")
    print()
