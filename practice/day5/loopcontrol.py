# 1-10 for 반복문을 사용하여 홀수만 출력
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

###
# animal = ['monkey', 'duck', 'cat', 'dog', 'giraffe', 'donkey','mouse']
# 6글자인 동물만 출력
# HINT : if, len(), continue
# ###

# animal = ['monkey', 'duck', 'cat', 'dog', 'giraffe', 'donkey', 'mouse']
#
# for ani in animal:
#     if len(ani) == 6:
#         print(ani)
#     else:
#         continue
#
# for i in range(len(animal)):
#     if len(animal[i]) == 6:
#         print(animal[i])
#     else:
#         continue


###
# DIFFICULT
# animal = ['monkey', 'duck', 'cat', 'dog', 'giraffe', 'donkey','mouse']
# 항목의 첫글자가 d인 항목만 출력
# ###

animal = ['monkey', 'duck', 'cat', 'dog', 'giraffe', 'donkey', 'mouse']

for ani in animal:
    # if ani[0] == 'd':
    if ani[0:1] == 'd':
    # if ani[:1] == 'd':
    # if ani[:2] == 'do':
    # if ani.startswith("d"):
        print(ani)
    else:
        continue

for i in range(len(animal)):
    # if animal[i][0] == 'd':
    if animal[i][0:1] == 'd':
    # if animal[i][:1] == 'd':
    # if animal[i].startswith("d"):
        print(animal[i])
    else:
        continue
