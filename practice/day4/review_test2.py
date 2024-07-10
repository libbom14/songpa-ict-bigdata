###
# 사용자로부터 문자열 데이터를 입력받아 format 함수를 이용하여 실행결과와 같이 출력
# ###

name = input("당신의 이름:")
best_friend = input("Best friend 배우 이름:")
movie = input("출연 영화:")

# text = "{}씨가 출연한 영화는 {}로 배우 {}씨와 함께 출연했습니다.".format(name, movie, best_friend)
text = "{name}씨가 출연한 영화는 {movie}로 배우 {best_friend}씨와 함께 출연했습니다.".format(name=name, movie=movie, best_friend=best_friend)

print(text)
