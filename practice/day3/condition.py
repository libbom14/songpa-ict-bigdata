# page 53 나이 문제
#
# age = int(input("Enter your age:"))
# if age >= 20 and age < 30:
# # if 20 <= age < 30:
#     print("You are a 20대")
# else:
#     print("20대가 아닙니다")

# 입력받은 숫자의 홀짝 여부
# num = int(input("Enter a number: "))
# if num % 2:
#     print(f"입력한 숫자 {num}는 홀수입니다.")
# else:
#     print(f"입력한 숫자 {num}는 짝수입니다.")


# 입력받은 숫자의 양수, 음수, 0(zero) 판별 여부
# num = int(input("Enter a number: "))
# if num == 0:
#     print(f"입력한 숫자 {num}는 zero입니다.")
# elif num > 0:
#     print(f"입력한 숫자 {num}는 양수입니다.")
# else:
#     print(f"입력한 숫자 {num}는 음수입니다.")


# 입력받은 도시
city = input("Enter city name: ")
if city == "서울":
    print("seoul시민")
elif city == "인천":
    print("incheon시민")
elif city == "부산":
    print("busan시민")
elif city == "대구":
    print("대구시민")
else:
    print("에러~~")

# citymap = {'서울': 'seoul', '인천': 'incheon', '부산': 'busan', '대구': '대구'}
# if citymap.get(city):
#     print(citymap.get(city)+"시민")
# else:
#     print("에러~~")
