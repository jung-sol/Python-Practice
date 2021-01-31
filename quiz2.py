# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# ex) https://naver.com

# 규칙1 : https:// 제외
# 규칙2 : 처음 만나는 . 이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자수 + 글자 내 'e' 갯수 + '!' 로 구성

# ex) nav51!

address = 'https://naver.com'

pw = address.split('https://')[1].split('.')[0]
print(pw[:3] + str(len(pw)) + str(pw.count('e')) + '!')

