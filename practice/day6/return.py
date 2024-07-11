###
# 함수를 호출하여 두개의 숫자를 함수 정의영역에서 입력받은 후, 두 정수에 대한 합을 구한 후, 결과값을 함수 호출영역으로 반환하여 출력하도록 프로그램을 작성하시오.
# def add():
#     어떤 수? 10,20
# [실행결과]
# add()
# 두수의 합=30
# ###

def add1():
    num1, num2 = map(int, input("어떤 수?").split(","))
    print("두수의 합={}".format(num1 + num2))


def add2():
    num1, num2 = map(int, input("어떤 수?").split(","))
    # sum = num1 + num2
    # return sum
    return num1 + num2


add1()

# result = add2()
# print("두수의 합={}".format(result))
print("두수의 합={}".format(add2()))
