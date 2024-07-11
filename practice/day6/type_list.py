# 예제

flowers = []
print(type(flowers))
# 데이터 추가
flowers.append("해바라기")
flowers.append("라일락")
flowers.append("장미")
flowers.append("코스모스")
flowers.append("백합")
flowers.append("수선화")
print(flowers)

# 라일락 -> 라벤더
flowers[1] = "라벤더"
print(flowers)

# "목련"을 "백합" 항목 앞에 삽입
flowers.insert(4, "목련")
print(flowers)

# "백합"을 삭제
flowers.remove("백합")
print(flowers)

# "수선화" 꽃을 검색하여 항목 삭제
flowers.remove("수선화")
print(flowers)

# 맨 마지막 항목 삭제
flowers.pop()
print(flowers)

# 0번째 인덱스 삭제
del flowers[0]
print(flowers)

# flower 리스트 전체 비우기
flowers.clear()
print(flowers)

# flowers 완전 삭제. print시 에러 발생
del flowers

print("=========================================================")

### 응용문제
# global_city = [시드니, 부에노스아이리스, 오사카, 뉴욕, 토론도, 로마]
# 1. "뉴욕" 항목 삭제
# 2. "오사카" 항목을 도쿄로 수정
# 3. "방콕" 항목을 "로마" 항목 앞에 삽입
# 4. "파리" 항목을 추가
# 5. "시드니" 항목을 검색하여 삭제
# 6. 현재 남아있는 도시를 출력
# ###

global_city = ["시드니", "부에노스아이리스", "오사카", "뉴욕", "토론토", "로마"]
print(f"global_city = {global_city}")

# 뉴욕 삭제
global_city.remove("뉴욕")
print(f"1번 후 global_city = {global_city}")

# 오사카 -> 도쿄
global_city[2] = "도쿄"
print(f"2번 후 global_city = {global_city}")

# 방콕, 로마 앞에 삽입
global_city.insert(4, "방콕")
print(f"3번 후 global_city = {global_city}")

# 파리 추가
global_city.append("파리")
print(f"4번 후 global_city = {global_city}")

# 시드니 검색 후 삭제
if "시드니" in global_city:
    global_city.remove("시드니")
print(f"5번 후 global_city = {global_city}")

# 마지막 출력
for city in global_city:
    print(city)
print(f"검색된 항목 도시={len(global_city)}")
