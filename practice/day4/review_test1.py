###
# 사용자로부터 성인 인원, 어린이 입원 입장객수를 ,(콤마)로 구분하여 입력하여 변수에 저장한 후 실행결과와 같이 출력
# 성인 1인 입장요금 12,000원 어린이 1인 입장요금 3,000원
# ###
adult_fee = 12000
child_fee = 3000

adult, child = map(int, input("성인 인원, 어린이 인원 입력:").split(","))

adult_charge = adult * adult_fee
child_charge = child * child_fee
total = adult_charge + child_charge

print(f"""
성인 입장객 :  성인 {adult}인 입장 요금은 {adult_charge:,}원
어린이 입장객 :  어린이 {child}인 입장 요금은 {child_charge:,}원
지불요금 합계 : {total:,}원입니다.""")
