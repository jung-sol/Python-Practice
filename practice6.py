# 지역변수, 전역변수

gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("gun : " + str(gun))

# checkpoint(8)
# print(str(gun))

# 위 방법은 코드 관리가 어려워 권장되는 방식은 아님
# 아래 예시처럼 사용 권장

def checkpoint(gun, soldiers):
    gun = gun - soldiers
    print("gun : " + str(gun))
    return gun

gun = checkpoint(gun, 8)
print(str(gun))