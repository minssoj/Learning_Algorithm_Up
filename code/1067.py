# [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1067
'''
n = int(input())
print('minus' if n < 0 else 'plus')
print('even' if n % 2 == 0 else 'odd')