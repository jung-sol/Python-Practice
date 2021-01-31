# 가변인자

def profile(name, age, *langs):
    print('이름: {0} 나이: {1}'.format(name, age), end=" ")
    for lang in langs:
        print(lang, end=' ')
    print()

profile('정솔', 20, '1', '2', '3', '4')
profile('장골', 21, '1')