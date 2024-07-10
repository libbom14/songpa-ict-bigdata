# page 51 커피 문제

menu = (input("커피 메뉴?: "))
price = int(input("커피 가격?: "))
count = int(input("주문 수량?: "))
total = price * count
total_str = "{:,}".format(total)

print(f"{menu} {count}잔 가격은 {total:,}원입니다.")
print(f"{menu} {count}잔 가격은 {total_str}원입니다.")
