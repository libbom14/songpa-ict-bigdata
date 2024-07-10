# fruits = ['apple', 'orange', 'pear', 'pineapple', 'banana', '참외', '수박', '딸기', '메론', '오렌지']
#
# fruit = input("무슨 과일 좋아해?")
#
# if fruit in fruits:
#     print(f"당신이 좋아하는 과일 {fruit}는(은) fruits 항목에 있습니다.")
# else:
#     print(f"당신이 좋아하는 과일 {fruit}는(은) fruits 항목에 없습니다.")

flowers = ['장미', '코스모스', '아이리스', '튜울립', '해바라기']
flower = input('꽃이름?')

if flower in flowers:
    if flower == '장미':
        print(f"{flower}는 rose")
    elif flower == '코스모스':
        print(f"{flower}는 cosmos")
    elif flower == '아이리스':
        print(f"{flower}는 iris")
    elif flower == '튜울립':
        print(f"{flower}은 tulip")
    elif flower == '해바라기':
        print(f"{flower}는 sunflower")
else:
    print(f"{flower}은 항목에 없습니다ㅠㅠ")


flowers_eng = {'장미': 'rose', '코스모스': 'cosmos', '아이리스': 'iris', '튜울립': 'tulip', '해바라기': 'sunflower'}
if flower in flowers:
    print(f"{flower}는 {flowers_eng[flower]}")
else:
    print(f"{flower}은 항목에 없습니다ㅠㅠ")

