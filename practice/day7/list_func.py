# flowers=[iris,rose,cosmos,sunflower,canna,tulip]

flowers = ["iris", "rose", "cosmos", "sunflower", "canna", "tulip"]
# 대문자로 변환하여 출력
for flower in flowers:
    print(flower.upper())

print("=" * 50)

# 오름차순으로 정렬하여 출력
sorted_flowers = sorted(flowers)
for flower in sorted_flowers:
    print(flower)

print("=" * 50)

# 항목과 글자의 개수를 출력
# 글자의 개수가 긴 순으로 동시에 출력

# 풀이1
sorted_flowers = sorted(flowers, reverse=True, key=len)
print(sorted_flowers)
flowers_c = list(map(len, sorted_flowers))
for i in range(len(flowers)):
    print(f"{sorted_flowers[i]:<20}\t{flowers_c[i]}")

# 풀이2
flowers_len = list(map(len, flowers))
flowers_zip = list(zip(flowers, flowers_len))
for i, j in sorted(flowers_zip, key=lambda x: x[1], reverse=True):
    print(f"{i:<20}\t{j}")
