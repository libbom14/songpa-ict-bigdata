# page 106 5번 문제
# 수선화만 출력되지 않도록
flowers = ["장미", "백합", "튤립", "국화", "수선화"]
for flower in flowers:
    if len(flower) == 2 or flower != "수선화":
        print(flower)

print("=========================================================")

# page 106 6번문제
city = ["경주", "부산", "파주", "대전", "전주", "진주", "영주", "남양주"]
for ju in city:
    if ju[-1] == "주":
        print(ju)

print("=========================================================")

# page 106 7번 문제
globalCity = ["시드니", "뉴욕", "벤쿠버", "부에노스아이레스", "모스크바", "브라질리아"]
globalCity_c = list(map(len, globalCity))
for i in range(len(globalCity)):
    print(f"{globalCity[i]:<20}\t{globalCity_c[i]}")
