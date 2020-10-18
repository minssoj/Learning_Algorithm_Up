# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1070
'''
m = int(input())
if m in [12, 1, 2]: print('winter')
elif m in [3, 4, 5]: print('spring')
elif m in [6, 7, 8]: print('summer')
else: print('fall')