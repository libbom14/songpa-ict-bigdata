###
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#
#     mo = num1 / num2
#     na = num1 % num2
#     print(f"{mo}...{na}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없어요.")
# else:
#     print("저는 정상적으로 동작해요.")
# finally:
#     print("퐈이널리~ 저는 에러 유무와 상관없이 무조건 출력되요.")
###

### page 110 진단문제
# 리스트 변수 listStr=["python", "programming", "seoul", "korea", "university"] 에
# 인덱스 위츼를 입력하여 해당 인덱스 위치에 있는 항목의 글자 길이를 구하는 프로그램을 작성하시오.
# 단, 해당 인덱스가 없다면 예외처리를 실행하시오.
# ###
listStr = ["python", "programming", "seoul", "korea", "university"]
while True:
    try:
        idx = int(input("인덱스?"))
        print(f"{listStr[idx]} ...{len(listStr[idx])}글자")
    except IndexError:
        print("해당 인덱스가 없습니다.")
        break
