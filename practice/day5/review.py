###
# 4. for 반복문을 이용하여 실행결과와 같이 출력
# 어떤숫자? 10
# 1+2+3+4+5+...10=55
# ###

num = int(input("합계를 구할 어떤 숫자?"))
sum = 0
for i in range(1, num + 1):
    sum += i
    if i == num:
        print(f"{i}={sum}")
    else:
        print(i, end="+")

###
# 5. while 반복문을 이용하여 어떤 숫자를 입력받아, 홀수인지, 짝수인지를 판별하여 홀수 개수와 짝수 개수를 출력하시오.
#     (단, 0이 입력되면 입력을 종료한다.)
#     어떤수?3
#     어떤수?7
#     어떤수?22
#     어떤수?9
#     어떤수?12
#     어떤수?0
#     홀수 개수=3
#     짝수 개수=2
#     ###

odd_cnt = 0
even_cnt = 0
while True:
    num = int(input("어떤 숫자?"))
    if num == 0:
        print(f"홀수 개수={odd_cnt}\n짝수 개수={even_cnt}")
        break
    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
