# [기초-2차원배열] 바둑알 십자 뒤집기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1097
'''
m = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for j in range(n):
    a, b = map(int, input().split())
    for i in range(19): m[a-1][i] = int(not(m[a-1][i]))
    for i in range(19): m[i][b-1] = int(not(m[i][b-1]))

for j in range(19):
    for i in range(19):
        print(m[j][i], end=' ')
    print()
