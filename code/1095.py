# [기초-1차원배열] 이상한 출석 번호 부르기3(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1095
'''
n = int(input())
m = list(map(int, input().split()))

min = 23
for i in range(n): min = (m[i] if m[i] < min else min)
print(min)