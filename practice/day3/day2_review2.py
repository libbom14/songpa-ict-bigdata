###
# 사용자로부터 3과목의 점수를 입력받아 총점과 평균
# 당신의 국어,영어,수학점소는?
# 실행결과
# 총점=240
# 평균=80
###

# kor, eng, math = input("Enter your score(kor,eng,math): ").split(",")
# total = int(kor) + int(eng) + int(math)

kor, eng, math = map(int, input("Enter your score(kor,eng,math): ").split(","))
total = kor + eng + math
avg = int(total / 3)
print(f"1. 총점={total}\n평균={avg}")
print("2. 총점={}\n평균={}".format(total, avg))
print("3. 총점=%d\n평균=%d" % (total, avg))
