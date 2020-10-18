# [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1063
* 삼항 연산자
https://wikidocs.net/20701
'''
a, b = map(int, input().split())
print(a if a > b else b)