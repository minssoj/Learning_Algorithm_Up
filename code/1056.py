# [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1056
'''
n1, n2 = map(int, input().split())
print(int((n1 and (not n2)) or ((not n1) and n2)))