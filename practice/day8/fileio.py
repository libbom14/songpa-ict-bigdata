# try:
#     fr = open('file_example.txt', 'r', encoding='utf-8')
#     aa = fr.readlines()
#     for i in aa:
#         # print(i, end="")
#         print(i.strip())
# except FileNotFoundError:
#     print('File not found')

# while & readline 활용
# try:
#     fr = open('file_example.txt', 'r', encoding='utf-8')
#     aa = fr.readline()
#     while aa != "":
#         print(aa.strip())
#         aa = fr.readline()
#     # 겍체 종료
#     fr.close()
# except FileNotFoundError:
#     print('File not found')

# while & readlines 활용
# try:
#     fr = open('file_example.txt', 'r', encoding='utf-8')
#     aa = fr.readlines()
#     while aa:
#         for i in aa:
#             print(i.strip())
#         break
#     fr.close()
# except FileNotFoundError:
#     print('File not found')
#
# # readlines 활용 & while count
# try:
#     fr = open('file_example.txt', 'r', encoding='utf-8')
#     aa = fr.readlines()
#     cnt = 0
#     while cnt < len(aa):
#         print(aa[cnt].strip())
#         cnt += 1
#         break
#     fr.close()
# except FileNotFoundError:
#     print('File not found')

# 예제 구구단, 구구단 추가
# try:
#     fw = open('file_gugudan.txt', 'a+', encoding='utf-8')
#     gugu = int(input("구구단 몇단?"))
#
#     for i in range(1, 10, 1):
#         # 구구단을 파일에 쓰기!
#         fw.write(f"{gugu} * {i} = {gugu * i}\n")
#     fw.close()
# except FileNotFoundError:
#     print('File not found')

# page 119 진단문제

name = input("이름:")
hobby = input("취미:")
age = input("나이:")

try:
    fw = open('file_whoami.txt', 'a+', encoding='utf-8')
    fw.write(f"이름:{name}\n취미:{hobby}\n나이:{age}\n")
    fw.close()
except FileNotFoundError:
    print('File not found')
