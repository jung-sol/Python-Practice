# 당신은 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이
# 조건2 : 당신은 소요 시간이 5분 ~ 15분 사이의 승객만 매칭합니다.
from random import *
count = 0

for index in range(1, 51):
    during_time = randrange(1, 51)
    
    if int(during_time) >= 5 and int(during_time) <= 15:
        is_custom = 'O'
        count += 1
    else:
        is_custom = ' '
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(is_custom, index, during_time))

print("총 탑승 승객 : {0} 명".format(count))