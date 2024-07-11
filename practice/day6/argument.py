###
# a,b 변수에 10,20 데이터를 기억 한 후, 함수를 호출 시 인자값을 전달하여 두 수에 대한 합을 구하는 함수
# ###
# ###
# def add(x,y):
#    return x + y
###

###
# 함수 호출 영역에서 사용자로부터 어떤 수를 입력받은 후,
# 입력받은 정수를 인자로 함수를 호출 한 후
# 1-어떤수(n)까지 합을 구하는 함수 호출 영역에서 출력하는 함수
#
# 어떤수? 10
# 1-10까지 합=55
# ###

def sum_number(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result


num = int(input("어떤 수까지의 합을 구할까요? : "))
print(f"1-{num}까지의 합 = {sum_number(num)}")


###
# 사용자로부터 어떤 두 수를 입력받아, 매개변수로 함수를 호출하여
# 작은수부터 큰수까지의 합을 구하는 프로그램을 작성하시오.
# 작은수는 if 조건으로 판단해서 사용해도 되지만, 편의를 위해 작은수,큰수로 함
# ###

def sum_range(num1, num2):
    result = 0
    for i in range(num1, num2 + 1):
        result += i
    return result


x, y = map(int, (input("어떤 수부터 어떤 수까지의 합을 구할까요? : ").split(",")))
print(f"{x}-{y}까지의 합 = {sum_range(x, y)}")
