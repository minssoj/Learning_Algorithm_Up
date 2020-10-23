# [기초-1차원배열] 이상한 출석 번호 부르기2(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1094
'''
n = int(input())
m = list(map(int, input().split()))

for i in range(n-1, -1, -1): print(m[i], end=' ')