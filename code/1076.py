# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1076
'''
n = ord(input())
# print(ord('a')) # a의 아스키코드 : 97
i = 97
while i <= n:
    print(chr(i), end=' ')
    i += 1
