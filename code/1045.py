# [기초-산술연산] 정수 2개 입력받아 자동 계산하기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1045
'''
s1, s2 = input().split()
n1 = int(s1)
n2 = int(s2)
print('{}\n{}\n{}\n{}\n{}\n{:.2f}'.format(n1+n2, n1-n2, n1*n2, n1//n2, n1%n2, n1/n2))

