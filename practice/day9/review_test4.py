# 함수 호출 영역에서 사용자로부터 문자 하나를 입력받아 함수 호출시 인자와 함께 전달하여 함수를 호출하고,
# 함수 정의 영역에서는 전달받은 매개변수가 알파벳 대문자인지, 소문자인지를 판별한 후,
# 판별한 결과를 반환하여 함수 호출영역에서 출력하는 함수 프로그램을 작성하시오.

def letter_case(letter):
    result = ""
    if letter.isupper():
        # if letter == letter.upper():
        result = "대문자"
    elif letter.islower():
        result = "소문자"
    elif letter.isdigit():
        result = "숫자"
    else:
        result = "몰?루"
    return result


def character(ch):
    if 'A' <= ch <= 'Z':
        result = '대문자'
    elif 'a' <= ch <= 'z':
        result = '소문자'
    else:
        result = '알파벳이 아님'
    return result


alphabet = input("알파벳 입력:")
print(f"입력한 알파벳 문자 {alphabet}는 {letter_case(alphabet)}")
print("입력한 알파벳 문자 {}는 {}".format(alphabet, letter_case(alphabet)))
print("입력한 알파벳 문자 {}는 {}".format(alphabet, character(alphabet)))
