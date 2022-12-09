# n = 0

# for i in range(10):
#     n = n + (i + 1)
#     print(n) 

# print(n)
import random

who = ["명석", "지현", "홍석", "서윤"]
where = ["화장실", "교실", "운동장", "편의점"]
what = ["양말", "지우개", "샤프심", "교통카드가"]

suspects = [who, where, what]
clues = []

for clue in suspects:
    clues.append(random.choice(clues))

print(f"{clues[0]}(이)가 {clues[1]}에서 {clues[2]}(으)로 사람을 죽임")



# ?? 이 ??에서 ??으로 사람을 죽였다


