# [기초-종합] 함께 문제 푸는 날(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1092
'''
d = list(map(int, input().split()))
i = 0
while True:
    i += 1
    if i%d[0] == 0 and i%d[1] == 0 and i%d[2] == 0:
        print(i)
        break