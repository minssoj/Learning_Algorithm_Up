# [기초-종합] 16진수 구구단?
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1082
'''
n = int(input(), 16)

for i in range(1, 16):
    print('{:X}*{:X}={:X}'.format(n, i, n*i))