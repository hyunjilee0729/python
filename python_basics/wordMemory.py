kor = open("wordKor.txt", "a", encoding = "UTF-8")
eng = open("wordEng.txt", "a", encoding = "UTF-8")

selct = 0
#단어입력
def word_in():
    kor = open("wordkor.txt", "a", encoding = "UTF-8")
    eng = open("wordEng.txt", "a", encoding = "UTF-8")
    while True:
        kor_in = input("한글뜻을 입력하세요(입력종료 : q)")
        if kor_in == "q":
            break
        else:
            kor.write(kor_in + "\n")
        eng_in = input("영어단어를 입력하세요(입력종료: q)")
        if eng_in == "q":
            break
        else:
            eng.write(eng_in + "\n")
    kor.close()
    eng.close()

#단어시험
def eng_exam():
    kor = open("wordkor.txt", "r", encoding = "UTF-8")
    eng = open("wordEng.txt", "r", encoding = "UTF-8")
    kor_Q = kor.readlines()
    eng_A = eng.readlines()
    score = 0

    for i in range(len(kor_Q)):
        answer = input(f"{kor_Q[i].strip()} 의 영어단어를 쓰시오 (종료: q) : ") 
        if answer == "q":
            break
        elif answer == eng_A[i].strip():
                print("정답!")
                score += 1
        else:
            print(f"땡! wjdekqdms {eng_A[i].strip()}")
    print("수고하셨습니다!")
    print(f"{len(kor_Q)} 문제중 {score} 문제를 맞췄습니다!")
    kor.close()
    eng.close()

while True:
    selct = int(input("1.단어입력 / 2.단어시험 / 3.종료"))
    if selct == 1:
        word_in()
    elif selct == 2:
        eng_exam()
    elif selct == 3:
        break
    else:
        print("잘못입력하셨습니다..")