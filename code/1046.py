# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1046
'''
n1, n2, n3 = map(int, input().split())
s = n1 + n2 + n3
print('{}\n{:.1f}'.format(s, s/3))