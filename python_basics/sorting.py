import random
def sorting(length):
    numbers = []
    num = 0
    numbers.append(random.randint(1, 1000))
    while len(numbers) < length:
        num = random.randint(1, 1000)
        if num in numbers:
            continue
        else:
            numbers.append(num)
    print(numbers)
    count = 0
    while True:
        shift = 0
        for i in range(len(numbers) - 1 ):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                shift += 1
                count += 1
        if shift == 0:
            break
    print(numbers)
    print(f"{count}번 만에 정렬 완료")
number = int(input("몇개의 숫자를 만드시겠습니까? : "))
sorting(number)