# name = input("Enter your name: ")  # 사용자로부터 이름을 입력받아 name 변수에 저장
# age = input("Enter your age: ")  # 사용자로부터 나이를 입력받아 age 변수에 저장
# print(f"Your name is {name} and your age is {age}")

"""
사용자로부터 3과목의 정수를 데이터로 입력받아 변수에 할당
총점과 평균을 구한 후, 평균이 80점 이상인 데이터에 대해서 그 결과를 Bool 자료형으로 출력하시오.
단, 평균은 정수 데이터만 출력
[Hint]
kor=int(input("국어점수:")) input() 문자로 인식
"""

kor = int(input("국어 점수?: "))
eng = int(input("영어 점수?: "))
math = int(input("수학 점수?: "))
total = kor + eng + math
avg = int(total / 3)
result = avg > 80

print(f"""
국어: {kor}
영어: {eng}
수학: {math}
총점: {total}
평균: {avg}
판정: {result}
""")
