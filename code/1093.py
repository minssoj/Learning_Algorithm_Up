# [기초-1차원배열] 이상한 출석 번호 부르기1(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1093
'''
n = int(input())
m = list(map(int, input().split()))

l = [0 for i in range(23)]

for i in range(n): l[m[i]-1] += 1
for i in range(23): print(l[i], end=' ')