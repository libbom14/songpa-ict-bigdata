###
# 국어 점수 80, 영어 점수 70, 수학 점수 70
# 총점, 평균 구해서 출력하는 문제
###

korean = 80
english = 70
mathematics = 70
total = korean + english + mathematics
average = total / 3
string = f"국어={korean}\n영어={english}\n수학={mathematics}\n총점={total}\n평균={average:.2F}"
print(string)

print(f"""
국어:{korean}
영어:{english}
수학:{mathematics}
총점:{total}
평균:{average:.2F}
""")

