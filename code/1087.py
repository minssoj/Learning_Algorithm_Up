# [기초-종합] 여기까지! 이제 그만~(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1087
'''
n = int(input())
i = 1
sum = 0

while True:
    sum += i
    if sum >= n:
        print(sum)
        break
    i += 1