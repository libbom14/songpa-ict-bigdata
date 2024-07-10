###
# 사칙연산자를 활용하여 실행결과 출력
# ###

num1 = 35
num2 = 8

print("덧셈 :", num1 + num2)
print("뺄셈 :", num1 - num2)
print("곱셈 :", num1 * num2)
print("나눗셈(몫) :", num1 // num2)
print(f"{num1}/{num2} : {num1 // num2} .. {num1 % num2}")

add = num1 + num2
mul = num1 * num2
div = num1 // num2
mod = num1 % num2

print(f"""
덧셈={add}
곱셈={mul}
나눗셈={div}
{num1}/{num2}={div}...{mod}
""")
