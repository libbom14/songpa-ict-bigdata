# 응용
# 1. flower_r.txt 파일을 읽어서 대문자로 변환하여 실행결과와 같이 flower_w.txt 파일을 생성하는 프로그램을 작성
#   [실행결과] : flower_w.txt 파일을 열었을때 아래와 같이 변환된 문자열이 나와야 함
#   ROSE
#   COSMOS
#   LILY
#   POPPY
#   DAISY
# 2. score.txt 파일을 읽어서 합계, 평균을 구하는 프로그램 작성
# 3. score_1.txt 파일을 읽어서 합계, 평균을 구하는 프로그램 작성
# 4. temperature.txt 파일을 읽어서 page 124 4번 문제 실행결과와 같이 지역에 대한 월 평균 기온을 출력하는 프로그램을 작성)

# 응용1
try:
    file1_read = open('../file_processing/flower_r.txt', 'r', encoding='utf-8')
    file1_write = open('../file_processing/flower_w.txt', 'w', encoding='utf-8')
    flowers = file1_read.readlines()
    for flower in flowers:
        file1_write.write(flower.strip().upper() + "\n")
    file1_read.close()
    file1_write.close()
    print("응용1 파일 생성 완료")
except FileNotFoundError:
    print("File not found")

print("=" * 50)

# 응용2
try:
    file2 = open('../file_processing/score.txt', 'r', encoding='utf-8')
    score = file2.readlines()
    score_sum = 0
    for i in score:
        i2 = i.strip()
        score_sum += int(i2)
    print(f"합계={score_sum}\n평균={int(score_sum / len(score))}")
    file2.close()
except FileNotFoundError:
    print("File not found")

print("=" * 50)

# 응용3
try:
    file3 = open('../file_processing/score_1.txt', 'r', encoding='utf-8')
    score_1_list = file3.readlines()
    sum_score_1 = 0
    print("이 름\t점수")
    print("=" * 10)
    for i in score_1_list:
        name, score2 = i.strip().split(",")
        sum_score_1 += int(score2)
        print(f"{name}\t{score2}")
    file3.close()
    avg_score_1 = int(sum_score_1 / len(score_1_list))
    print("=" * 10)
    print(f"합계: {sum_score_1}\n평균: {avg_score_1}")
except FileNotFoundError:
    print("File not found")

print("=" * 50)

# 응용4
try:
    file4 = open('../file_processing/temperature.txt', 'r', encoding='utf-8')
    weather_list = file4.readlines()
    for temperature in weather_list:
        city, minimum_temp, maximum_temp = temperature.split(" ")
        avg_temp = (float(minimum_temp) + float(maximum_temp)) / 2
        print(f"{city} 평균 기온은 {avg_temp:.2f}도 이다")
    file4.close()
except FileNotFoundError:
    print("File not found")
