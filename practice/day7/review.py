# 응용 1
# num=[5,1,2,7,9,8]에서 함수를 이용하여 합계와 평균을 실행결과와 같이 출력
# [실행결과]
# 합계=32
# 평균 5.33333

def review1(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    print(f"합계={total}")
    print(f"평균={avg:.5F}")


numbers = [5, 1, 2, 7, 9, 8]
review1(numbers)


def review2(*args):
    # 다중인자를 활용한 함수
    total = 0
    for number in args:
        total += number
    avg = total / len(args)
    print(f"합계={total}")
    print(f"평균={avg:.5F}")


review2(5, 1, 2, 7, 9, 8)

print("="*30)

# 응용 2
# animal=["goat", "sheep", "dunkey", "camel","kangaroo"] 에서
# 1) giraffe 를 마지막 항목에 추가
# 2) camel 항목이 존재한다면 삭제
# 3) 존재하고 있는 항목 개수를 출력
#   항목개수=4개

animal = ["goat", "sheep", "dunkey", "camel", "kangaroo"]
animal.append("giraffe")
if "camel" in animal:
    animal.remove("camel")
for ani in animal:
    print(ani)
print(f"====================")
print(f"항목개수={len(animal)}")
