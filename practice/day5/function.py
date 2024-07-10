# 사용자 정의 함수
#   def 함수명():
#        ~~~
# 함수 호출
#   함수명()
#
# def expert():
#     for i in range(5):
#         print("나는 빅데이터 전문가랍니다!")
#
#
# expert()

# ==============================================

###
# 구구단을 호출하여 구구단을 출력하는 함수 프로그램 작성
# ###

# def gugudan(num):
#     for i in range(1, 10):
#         print(f"{num} * {i} = {num * i}")
#
#
# num = int(input("구구단?"))
# gugudan(num)


# ==============================================

###
# 팩토리얼
# def factorial():
# ###

def factorial():
    result = 1
    num = int(input("원하는 팩토리얼 값은?"))
    # for i in range(1, num + 1):
    #     result *= i
    for i in range(num, 0, -1):
        result *= i
    print(f"{num}! = {result}")


factorial()
