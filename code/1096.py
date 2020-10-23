# [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1096
'''
m = [[0 for col in range(19)] for row in range(19)]
n = int(input())

for _ in range(n):
    j, i = map(int,input().split())
    m[j-1][i-1] = 1
for j in range(19):
    for i in range(19):
        print(m[j][i], end=' ')
    print()