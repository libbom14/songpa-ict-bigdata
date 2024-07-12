### page 105 3번 문제
#
# HINT
# 1) 다중리스트튜플을 딕셔너리 자료형으로 변환하기 위해서는 dict(다중리스트변수)fmf tkdyd
# 2) lambda 함수를 이용한 정렬
#   새로운변수 = sorted(변수, key=lambda x:x[인덱스], reverse=True/False)
#
# 문제해결을 위한 HINT
# 1. 다중리스트를 lambda 함수를 이용해서 sort
# 2. 다중리스트를 dict()함수를 사용하여 딕셔너리 자료형으로 변환
# 3. 반복문을 이용하여 출력
# 4. 순위는 임의변수 r=0으로 초기화 시킨 후, 해당 항목 출력에서 증가변수 r=r+1을 증가시켜 이용
###

movieList = [('오징어게임', 50.45), ('이터널스', 35.46), ('그레비티', 9.8), ('노타임투다이', 52.5), ('스파이더맨', 15.47)]

sortedMovieList = sorted(movieList, key=lambda x: x[1], reverse=True)

dictMovie = dict(sortedMovieList)
print("list형 movie: \n", sortedMovieList)
# [('노타임투다이', 52.5), ('오징어게임', 50.45), ('이터널스', 35.46), ('스파이더맨', 15.47), ('그레비티', 9.8)]
print("dictionary형 movie: \n", dictMovie)
# {'노타임투다이': 52.5, '오징어게임': 50.45, '이터널스': 35.46, '스파이더맨': 15.47, '그레비티': 9.8}

print("=" * 50)

rank = 0
print("영화제목\t\t\t\t예매율\t순위")
print("========\t\t\t======\t====")
for title, rate in dictMovie.items():
    rank += 1
    print(f"{title:10}\t{rate:8}\t{rank}")
