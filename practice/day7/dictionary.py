grade = {}
grade["아이키"] = 90
grade["박보검"] = 95
grade["유아인"] = 80
grade["전지현"] = 100
grade["송중기"] = 90
print(grade)
print(grade.keys())
print(grade.values())
print(grade.items())

# 응용1: 저장된 grade 딕셔너리 자료형에서 key와 value 값을 동시에 멋지고 세련되게 출력
# 아이키       90
# 박보검       95
# 유아인       80
# 전지현       100
# 송중기       90

# 풀이1
for i in grade.keys():
    print(i, grade[i])
# 풀이2
for key, value in grade.items():
    print(key, "\t", value)

print("=" * 50)

# 응용2: 유아인의 점수 80점을 85점으로 수정
grade['유아인'] = 85
print(grade)

print("=" * 50)

# 응용3: 유아인 점수가 수정된 상태에서 grade 자료형의 value 값에 대한 합계
print("grade value 합계 :", sum(grade.values()))
