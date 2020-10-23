# [기초-2차원배열] 설탕과자 뽑기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1098
'''
h, w = map(int, input().split())
m = [[0 for i in range(w)] for i in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for i in range(l): m[x-1+(i*d)][y-1+(i*(1-d))] = 1
for j in range(h):
    for i in range(w):
        print(m[j][i], end=' ')
    print()