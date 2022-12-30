def enter (text):
    result = text + "\n"
    return result

e = open("eng.text", "a", encoding = "UTF-8")
k = open("kor.text", "a", encoding = "UTF-8")


while True:
    sel = input("단어입력 - i / 끝내기 - q / 단어시험 - t")
    if sel == "i":
    #영어단어 입력받기
        word_E = input("영어단어를 입력하세요 : ")
        e.write(enter(word_E))
    #한글 뜻 입력받기
        word_K = input("한글 뜻을 입력하세요 : ")
        k.write(enter(word_K))
    elif sel == "q":
        break
    elif sel == "t":
        e = open("eng.text", "r", encoding = "UTF-8")
        k = open("kor.text", "r", encoding = "UTF-8")
        kors = k.readlines()
        engs = e.readlines()
        for i in range(len(kors)):
            answerQ = input(f"{kors[i]} 뜻을 가진 영어단어는? : ")
            answerA = engs[i].strip()
            if answerQ == answerA:
                print("정답!")
            else:
                print(f"틀렸습니다. 정답은 {engs[i]} 입니다")
        e.close()
        k.close()
