# page 55 두개의 조건 만족하면 로그인 성공, 틀리면 해당 오류 안내
id = input("Enter your 학교코드 : ")
pw = input("Enter your 패스워드 : ")

if id == "hankook":
    if pw == "hk1234":
        print("로그인 성공")
    else:
        print("패스워드 오류!")
else:
    if pw == "hk1234":
        print("학교코드 오류!")
    else:
        print("그냥 다 오류!")