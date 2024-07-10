###
# 밑변, 윗변, 높이를 입력받아 사다리꼴 넓이를 구해~
# 밑변,윗변,높이? 14,12,8
# 실행결과
# 사다리꼴 넓이= 104cm
#
# HINT
# 사다리꼴 넓이 = (밑변+윗변)*높이/2
###

# kor, eng, math = input("Enter your score(kor,eng,math): ").split(",")
# total = int(kor) + int(eng) + int(math)

top_width, bottom_width, height = map(int, input("사다리꼴?(밑변,윗변,높이): ").split(","))
area = int((top_width + bottom_width) * height / 2)
print(f"사다리꼴의 넓이 : {area}cm²")
