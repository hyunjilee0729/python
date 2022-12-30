f = open("test.txt," , "w", encoding = "UTF-8")
#파일을 새로 만들거나, 있는 파일을 덮어쓸때는 "w"
#기존 파일에 내용을 덧붙일때는 "a"
#기존 파일에서 내용을 읽어오기만 할때는 "r"

f.write("반갑습니다\n")
f.write("2022년이 얼마 안남았어요\n")
f.write("정말..주옥같네요\n")
#w나 a로 파일에 쓰기가 가능할 때 write 메서드로 내용을 적을 수 있음

f.close()

f = open("test.txt," , "r", encoding = "UTF-8")

line = f.readline()
lines = f.readlines()
print(line)
print(lines)

f.close()
#불러온 파일을 닫아줌
