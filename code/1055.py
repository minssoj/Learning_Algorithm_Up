# [기초-논리연산] 하나라도 참이면 참 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1055
'''
n1, n2 = map(int, input().split())
print(int(n1 or n2))