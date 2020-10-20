# [기초-종합] 3 6 9 게임의 왕이 되자!(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1083
'''
n = int(input())

for i in range(1, n+1):
    print('X', end=' ') if i % 3 == 0 else print(i, end=' ')

