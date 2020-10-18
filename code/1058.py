# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1058
'''
n1, n2 = map(int, input().split())
print(int(not (n1 or n2)))