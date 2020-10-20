# [기초-종합] 주사위를 2개 던지면?(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1081
'''
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i+1, j+1)