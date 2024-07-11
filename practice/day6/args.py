###
# 숫자 1,3,4,7,9,8,2,5,7 에 대한 숫자를 인자로 함수를 호출하여
# 다중인자에 대한 합을 합수 호출 영역에서 출력하도록
# ###

def multiNum(*args):
    sum = 0
    for num in args:
        # print(num)
        sum += num
    return sum


multiNum(1, 3, 4, 7, 9, 8, 2, 5, 7)
print("합 = {}".format(multiNum(1, 3, 4, 7, 9, 8, 2, 5, 7)))


###
# 아래 영화에 대한 문자열을 다중인자로 넘긴 후,
# 사용자 정의영역에서 글자의 개수와 함께 멋지게 출력
# 문자열 "범죄도시4", "인사이드아웃2", "하이재킹", "파묘", "서울의봄" ###

def multiMovie(*args):
    # for 반복문으로 데이터 값을 가져옴
    # 출력하되 글자개수와 함께
    for movie in args:
        print(f"{movie:<16}\t{len(movie)}")


multiMovie("범죄도시4", "인사이드아웃2", "하이재킹", "파묘", "서울의봄")


# page 67 출력 문제
def name_hobby(name, hobby):
    print(f"{name}은(는) 취미가 {hobby}이다.")


name = input("이름 : ")
hobby = input("취미 : ")
name_hobby(name, hobby)
