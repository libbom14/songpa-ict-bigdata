###
# 사용자로부터 전력용도, 사용량을 입력하여 전기요금을 산출하는 중첩 if문 프로그램을 작성
# 용도별 전기료 산출에 필요한 기본요금 및 kwh 전력량 요금은
# --------------------------------------------
#                 | 주택용 | 공업용 | 산업용 |
#       기본요금    |  190  | 1600 | 7300 |
#   kwh 전력량 요금  |  88  |  182 |  275 |
#   ###

purpose = input("용도 : 1:주택용, 2:공업용, 3:산업용?")
usage = int(input("사용량(kwh)?"))
e_bill = 0
bill_text = ""

# if purpose == "1":
#     e_bill = 190 + 88 * usage
#     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
# elif purpose == "2":
#     e_bill = 1600 + 182 * usage
#     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
# elif purpose == "3":
#     e_bill = 7300 + 275 * usage
#     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
# else:
#     bill_text = "용도를 맞게 입력해주세요."
# print(bill_text)

purpose_list = ["1", "2", "3"]
base_fee = {"1": 190, "2": 1600, "3": 7300}
usage_fee = {"1": 88, "2": 182, "3": 275}

if purpose in purpose_list:
    # if purpose == "1":
    #     e_bill = 190 + 88 * usage
    #     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
    # elif purpose == "2":
    #     e_bill = 1600 + 182 * usage
    #     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
    # elif purpose == "3":
    #     e_bill = 7300 + 275 * usage
    #     bill_text = f"용도:{purpose}, 사용량:{usage:.2F}, 전기요금:{e_bill:.2F}원"
    # else:
    #     bill_text = "용도를 맞게 입력해주세요."
    e_bill = base_fee[purpose] + usage_fee[purpose] * usage
    print(f"용도:{purpose}, 사용량:{usage:,.2F}, 전기요금:{e_bill:,.2F}원")
else:
    print("용도를 맞게 입력해주세요.")
