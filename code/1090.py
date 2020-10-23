# [기초-종합] 수 나열하기2
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1090
'''
a, r, n = map(int, input().split())
print(a * (r ** (n-1)))