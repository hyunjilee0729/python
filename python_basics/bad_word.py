from multiprocessing import connection


bad_words = ["시발", "ㅗ", "병신", "새끼", "개새끼", "지랄", "개소리", "시발놈", "또라이", "미친새끼"]
bad_word = []
answer = 0
add_word = 0

while True:
    answer = input("말씀하세요 주인님 : ")
    bad_word = []

    for word in bad_words:
        if word in answer:
            bad_word.append(word)
           
    if len(bad_word) > 0:
           print(f"{bad_word} (이)라는 말은 쓰면 안돼요. 지옥간다 이샛기야")
           continue
        
    else:
        if answer == "나가":
            print("좋은 하루 되세요!")
            break
        elif answer == "추가":
            add_word = input("어떤 단어를 추가할까요? : ")
            bad_words.append(add_word)
            print(f"{add_word} 단어가 추가되었습니다!")
            print(f"지금까지 등록된 금지어를 보여드리겠습니다!")
            print("=" * 50)
            print(bad_words)
            print("=" * 50)
            
        else:
            print(f"{answer} (이)라고요? 아이고 참 옳으신 말씀이십니다")