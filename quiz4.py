# 표준 체중을 구하는 프로그램을 작성하시오

# 남자 : 키(m) x 키 x 22
# 여자 : 키(m) x 키 x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         함수명 : std_weight
#         전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# ex ) 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == '여자':
        val = 21
    else:
        val = 22
    
    avg_weight = height * height * val
    return avg_weight

height = 175
gender = '남자'
avg_weight = round(std_weight(height / 100, gender), 2)
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, avg_weight))