# book 리스트에 저장된 문자열 항목에 대해서 문자열과 문자열 길이를 출력하되,
# 문자열 길이가 긴순으로 실행결과와 같이 출력
# book=["Java", "Python", "C", "SQL", "Pascal"]
# [실행결과]
# Python    6
# Pascal    6
# Java      4
# SQL       3
# C         1

book = ["Java", "Python", "C", "SQL", "Pascal"]
book_len = list(map(len, book))
book_zip = zip(book, book_len)
book_sort = sorted(book_zip, reverse=True, key=lambda x: x[1])
for book_name, length in book_sort:
    print(f"{book_name:<10}{length}")
