# [기초-종합] 3의 배수는 통과?(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1088
'''
n = int(input())
for i in range(1, n+1):
    if i % 3 !=0: print(i, end= ' ')
