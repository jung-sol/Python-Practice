print('나는 %d살 입니다.' % 1)
print('나는 %s을 좋아해요' % '파이썬')
print('나는 %c로 시작해요' % 's')
print('나는 %s색과 %s색을 좋아해요' % ('파란', '빨간'))

print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요' .format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요' .format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요' .format('파란', '빨간'))
print('나는 {blue}색과 {red}색을 좋아해요' .format(blue = '파란', red = '빨간'))

age = 20
color = '빨간색'

print(f'나는 {age}살이며 {color}를 좋아해요')