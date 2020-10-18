# [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1066
'''
n = list(map(int, input().split()))
for i in n:
    print('even' if i % 2 == 0 else 'odd')
