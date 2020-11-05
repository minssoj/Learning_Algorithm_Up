# 성적 계산
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1127
'''
score = 0
for _ in range(3):
    p, n = input().split()
    score += float(p) * int(n)
print('%.1f' %score)