# [기초-종합] 수 나열하기3
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1091
'''
a, m, d, n = map(int, input().split())
for i in range(n-1):
    a = a * m + d
print(a)