# 클래스
class Unit:
    def __init__(self, name, hp, damage):   # 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("이름: {0}, 공격력: {1}, 체력: {2}".format(self.name, self.hp, self.damage))

marine1 = Unit("마린", 40, 5)   # 객체 (클래스로부터 만들어지는 것)
marine2 = Unit("마린2", 40, 5)
tank = Unit("탱크", 140, 50)

# 마린과 탱크는 유닛의 인스턴스 라고 함

wraith1 = Unit("레이스", 80, 5)
print("유닛이름: " + wraith1.name)  # 멤버변수 외부에서도 사용 가능

# 클로킹 변수 외부에서 추가 가능
wraith2 = Unit("레이스2", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(wraith2.name + "은 클로킹 상태입니다.")