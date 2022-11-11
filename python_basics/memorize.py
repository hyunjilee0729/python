import random
import os
clear = lambda: os.system('cls')

eng = ["oxygen", "make a living", "greatly", "various", "wonder", "creature", "even", "show up", "appear", "surface"]
kor = ["산소", "생계를 꾸리다", "크게", "다양한", "궁금하다", "생물", "훨씬", "나타나다", "나타나다", "표면"]
select = 0
answer = 0
mode = 0

while True:
    clear()
    print("*" * 24)
    print("AI 영어단어봇V")
    print("*" * 24)
    print(f"수록 영어단어 갯수: {len(eng)}")
    print("*" * 24)
    mode = input("원하는 작업 선택: 단어시험 / 단어입력 / 종료 ")
    print("*" * 24)
    if mode == "단어시험":
        while len(kor) != 0: #모든 단어를 맞출 때 까지 반복하기
            clear()
            select = random.randint(0, len(eng) - 1 ) #단어 무작위로 물어보기
            answer = input(f"{kor[select]}이 단어를 영어로 하면? : ") #단어 무작위로 물어보기

            if answer == eng[select]:
                print(f"정답입니다~! {kor[select]} = {eng[select]} 입니다! ")
                eng.pop(select)
                kor.pop(select)
                #정답을 맞춘 단어는 목록에서 삭제하기
            else:
                print("안타깝게도 틀리셨습니다..")

        print("열개의 단어를 모두 맞추셨습니다!")

    elif mode == "종료":
        print("시스템을 종료합니다.")
        break

    elif mode == "단어입력":
        while True:
            eng.append(input("영어단어를 입력하세요 : ")) #영어단어 추가하기
            kor.append(input("한글단어를 입력하세요 : ")) #한글단어 추가하기
            if input("입력을 더 하시겠습니까? (예 / 아니오) "):
                print("단어입력을 마쳤습니다.")
                break
            
        #영어단어 입력
        #한글단어 입력


