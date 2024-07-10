###
# 사용자로부터 전국 지역별 전화번호를 입력받아 해당 지역번호에 맞는 지역을 실행결과와 같이 출력
# 지역별 전화번호 참고
# 서울특별시 02,
# 해당 지역번호가 없으면 '잘못된 지역번호'를 표시
# ###

area_codes = ["02", "031", "041", "043", "054", "055", "061", "063", "064"]
area_code = input("지역번호를 입력하세요:")
city_name = ""
if area_code in area_codes:
    if area_code == "02":
        city_name = "서울특별시"
    elif area_code == "031":
        city_name = "경기도"
    elif area_code == "041":
        city_name = "충청남도"
    elif area_code == "043":
        city_name = "충청북도"
    elif area_code == "054":
        city_name = "경상북도"
    elif area_code == "055":
        city_name = "경상남도"
    elif area_code == "061":
        city_name = "전라남도"
    elif area_code == "063":
        city_name = "전라북도"
    elif area_code == "064":
        city_name = "제주도"
else:
    city_name = "잘못된 지역번호"

print(city_name)
