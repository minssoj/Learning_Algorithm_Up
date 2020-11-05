# 분자량 구하기 1
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1124
'''
#C의 원자량은 12, H의 원자량은 1

'''
외부 모듈 사용 금지
from parse import *

s = input()
result = parse("C{}H{}", s)
c = result.fixed[0]
h = result.fixed[1]
print(12*int(c) + int(h))
'''
s = input()
num = list(map(int, s[1:].split('H')))
print(12 * num[0] + num[1])

