# [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1064
'''
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)