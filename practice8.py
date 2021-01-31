# 매서드
class Unit:
    def __init__(self, name, hp, damage):   # 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("이름: {0}, 공격력: {1}, 체력: {2}".format(self.name, self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):   # 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("이름: {0}, 공격력: {1}, 체력: {2}".format(self.name, self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. {2}".format(self.name, location, self.damage))    # location은 전달받은 값을 쓰고, 나머진 self에서 꺼내쓴다는 얘기
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재체력 : {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print(self.name + " 유닛이 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
    
