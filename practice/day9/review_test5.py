# 제공해드린 "sungjuk.txt" 파일을 읽어서
# 총점, 평균을 구하는 파일 프로그램을 작성
# 단, 평균은 소숫 둘째자리까지 출력

sungjuk_file = open("../file_processing/sungjuk.txt", "r", encoding="utf-8")
sungjuk_lines = sungjuk_file.readlines()

print("이름   점수1 점수2 점수3 총점  평균")
print("=" * 30)
for line in sungjuk_lines:
    score = line.split()
    total = int(score[1]) + int(score[2]) + int(score[3])
    avg = total / 3
    print(f"{score[0]}\t{score[1]}\t{score[2]}\t{score[3]}\t{total}\t{avg:.2F}")
sungjuk_file.close()
