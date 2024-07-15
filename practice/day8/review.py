###
# # 응용
# 아래와 같이 다중리스트 튜플에 대한 자료가 스택이름, 단가, 수량으로 차례로 저장되어 있다.
# snack=[('초코파이',3000,3),('새우깡',2700,8),('빼빼로',1900,7),('코코넛',2000,5),('칸초',1500,8)]
# 다중리스트 튜플에 대한 자료를 가지고 실행결과와 같이 출력
# [실행결과]
#   품목      단가    수량   금액
# ======    =====   === ======
# 초코파이    3,000   3   9,000
# 새우깡     2,700   8   21,600
# 빼뺴로     1,900   7   13,300
# 코코넛     2,000   5   10,000
# 칸초      1,500   8   12,000
# ###

snack_box = [('초코파이', 3000, 3), ('새우깡', 2700, 8), ('빼빼로', 1900, 7), ('코코넛', 2000, 5), ('칸초', 1500, 8)]

# 풀이1
print("  품목\t\t 단가\t수량\t\t금액")
print("======\t\t=====\t===\t ======")
total = 0
for snack in snack_box:
    print(f"{snack[0]:<10}{snack[1]:>5,}\t{snack[2]:>2}\t{snack[1] * snack[2]:>7,}\t")
    total += snack[1] * snack[2]
print("=" * 30)
print(f"스낵 물품 구입 금액\t\t\t{total:,}")

# 풀이2
print("  품목\t\t 단가\t수량\t\t금액")
print("======\t\t=====\t===\t ======")
price = 0  # 단가*수량
grand_total = 0  # price의 전체 누적
for pum, unit, qty in snack_box:
    price = unit * qty  # 단가*수량 을 price에 저장
    grand_total += price
    print(f"{pum:<10}{unit:,}\t{qty}\t{price:>6,}")
print("=" * 30)
print("\t\t스낵 물품 구입 금액:{grand_total:,}".format(grand_total=grand_total))
