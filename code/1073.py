# [기초-반복실행구조] 0 입력될 때까지 무한 출력하기2(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1073
'''
l = list(map(int, input().split()))
for i in l:
    if i == 0:
        break;
    print(i)