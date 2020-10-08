# [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1025
'''
num = input()
l = len(num)
for i, n in enumerate(num):
    print('['+ n + '0' * (l - i - 1) + ']')