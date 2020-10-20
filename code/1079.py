# [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1079
'''
s = list(input().split())

for i in s:
    print(i)
    if i == 'q':
        break