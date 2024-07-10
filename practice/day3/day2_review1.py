###
# 아래와 같이 사용자로부터 이름과 생년월일을 입력받아 실행결과와 같이 출력
# 이름? 홍길동
# 생년월일? 2000,7,6
# [실행결과]
# 홍길동군의 생년월일은 2000년 7월 6일입니다.
# Hint: 동시에 3개의 입력 데이터를 받기 위해서는 split() 사용
###

name = input("Enter your name: ")
# birthday = input("Enter your birthday(year,month,day): ")
# birthday_str = birthday.split(",")
# print(f"{name}군의 생년월일은 {birthday_str[0]}년 {birthday_str[1]}월 {birthday_str[2]}일입니다.")

year, month, day = input("Enter your birthday: ").split(",")
print(f"{name}군의 생년월일은 {year}년 {month}월 {day}일입니다.")
