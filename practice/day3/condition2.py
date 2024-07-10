# page 56 두과목 입력, 평균 점수에 따른 학점
score1, score2 = map(int, input("Enter score 1,2: ").split(","))
avg = int((score1 + score2) / 2)
grade = "F"
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

if avg % 10 >= 5:
    grade += "+"

print(f"avg {avg}: grade {grade}")
