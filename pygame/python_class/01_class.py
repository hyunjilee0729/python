class 캐릭터():
    def __init__(self, 체력, 공격력, 이속): #시작함수. mathod
        self.체력 = 체력
        self.공격력 = 공격력
        self.이속 = 이속

    def 사망(self):
        if self.체력 <= 0:
            print("사망했습니다")

    def 상태보기(self, name):
        print(name)
        print(f"체력 : {self.체력}")
        print(f"공격력 : {self.공격력}")
        print(f"이속 : {self.이속}")

class 챔피언(캐릭터): #상속. 괄호안이 super class 바깥이 sub class
    def __init__(self, 체력, 공격력, 이속, q, w, e, r):
        super().__init__(체력, 공격력, 이속) #super class의 mathod를 기능 업그레이드 하는 것: method override
        self.q = q
        self.w = w
        self.e = e
        self.r = r

    def 상태보기(self, name):
        super().상태보기(name)
        print(f"Q스킬 : {self.q}")
        print(f"W스킬 : {self.w}")
        print(f"E스킬 : {self.e}")
        print(f"R스킬 : {self.r}")

미니언01 = 캐릭터(100, 5, 20) #캐릭터 클래스를 이용해 미니언01이라는 인스턴스를 생성. 생성된 아이는 객체object
미니언01.상태보기("미니언1번의 상태") #미니언01의 상태보기 mathod를 호출
야스오 = 챔피언(100, 1000, 500, "찌르기", "장막", "돌진", "난도질") #캐릭터 클래스로부터 상속된 sub class 인 챔피언 클래스로 생성한 인스턴스
야스오.상태보기("야스오의 상태") #야스오의 상태보기 mathod를 호출

미니언01.체력 -=  야스오.공격력
미니언01.사망()