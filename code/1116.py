# 사칙연산 계산기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1116
'''
a, b = list(map(int, input().split()))
print('{}+{}={}'.format(a, b, a + b))
print('{}-{}={}'.format(a, b, a - b))
print('{}*{}={}'.format(a, b, a * b))
print('{}/{}={}'.format(a, b, a // b))