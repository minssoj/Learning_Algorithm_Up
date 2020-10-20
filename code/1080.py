# [기초-종합] 언제까지 더해야 할까?
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1080
'''
n = int(input())
sum = 0
i = 1

while True:
    sum += i
    if sum >= n:
        print(i)
        break
    i += 1