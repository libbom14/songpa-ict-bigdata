###
# 사용자로부터 밑변과 높이를 입력받아 삼각형의 넓이를 구하는 프로그램을 작성하시오.
# 단, 삼각형의 넓이는 소숫점 2자리까지 표시되도록 한다.
# HINT
# 삼각형의 넓이 = 밑변 * 높이 / 2
# ###

bottom = int(input("밑변 입력:"))
height = int(input("높이 입력:"))

triangle = bottom * height / 2

print(f"삼각형의 넓이 = {triangle:.2F}")
