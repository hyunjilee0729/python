from text_data_01 import questions_01 # 선배 지문
from text_data_02 import questions_02 # 동갑 지문
from text_data_03 import questions_03 # 후배 지문
from ending import * # 엔딩 지문

import os
clear = lambda: os.system('cls') # 화면청소기능

# 3명의 인물 선택지
women = ["선배", "동갑", "후배", "끝"]

  

# 화면구분 UI
def line():
    print("-" * 30)

# 메인질문 함수
def question10(woman): # woman 매개변수에 선택하는 인물 받음
    score = 0
    for question in woman: # 각 대상별 지문 가져오기
        clear()
        for i in question[0]: # 질문상황
            print(i)
            num = 1
        line()
        for answer in question[1]: # 질문내용
            print(f"{num}. {answer}")
            num += 1
        line()
        sel = int(input("1~4 중 하나를 선택 : ")) # 질문 중 하나 선택하기
        clear()
        print(f"주인공 : {question[1][sel-1]}") # 선택한 결과 주인공 대사
        print(f"상대방 : {question[2][sel-1]}") # 선택한 결과 상대방 대사s
        score += question[3][sel-1] # 각 질문별 점수 합산
        input("(다음으로 넘어가려면 엔터를 치세요...)")
    return score

love_score = 0
score1 = 0 # 인물별 성공/실패 여부
score2 = 0
score3 = 0  
success = 0
running = True

while running: 
    #누구와 연애를 할 지 선택
    if len(women) > 1:
        clear()
        print("이성에 눈을 뜬 주인공, 여자친구를 만들고 싶다")
        line()
        name_list = 1
        for name in women: # 연애대상 화면 출력
            print(f"{name_list}. {name}")
            name_list += 1
        line()
        choice = int(input("누구와 연애를 시작하시겠습니까? : "))
        chosen_woman = women.pop(choice-1) 
        if chosen_woman == "선배":
            love_score = question10(questions_01)
            if love_score >= 12: # 연애성공점수         
                score1 = 1
            else:
                score1 = 0
            clear()
            print(personal_ending1[score1])
            input("(다음으로 넘어가려면 엔터를 치세요...)")
        elif chosen_woman == "동갑":
            love_score = question10(questions_02)
            if love_score >= 12: # 연애성공점수
                score2 = 1
            else:
                score2 = 0 
            clear()
            print(personal_ending2[score2])
            input("(다음으로 넘어가려면 엔터를 치세요...)")
        elif chosen_woman == "후배":
            love_score = question10(questions_03)
            if love_score >= 12: # 연애성공점수
                score3 = 1
            else:
                score3 = 0
            clear()     
            print(personal_ending3[score3])
            input("(다음으로 넘어가려면 엔터를 치세요...)") 
        elif chosen_woman == "끝":
            running = False
    else:
        running = False
clear()

success = [score1, score2, score3]
# 연애 대상별/성공-실패별 최종결과 출력

if success[0] == 1 and success[1] == 1 and success[2] == 1:
    print(real_ending111)
elif success[0] == 0 and success[1] == 0 and success[2] == 0:
    print(real_ending000)
elif success[0] == 0 and success[1] == 0 and success[2] == 1:
    print(real_ending001)
elif success[0] == 0 and success[1] == 1 and success[2] == 1:
    print(real_ending011)
elif success[0] == 1 and success[1] == 1 and success[2] == 0:
    print(real_ending110)
elif success[0] == 1 and success[1] == 0 and success[2] == 1:
    print(real_ending101)
elif success[0] == 1 and success[1] == 0 and success[2] == 0:
    print(real_ending100)
elif success[0] == 0 and success[1] == 1 and success[2] == 0:
    print(real_ending010)
