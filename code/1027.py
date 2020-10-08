# [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1027
'''
y, m, d = input().split('.')
print('{:02d}-{:02d}-{:04d}'.format(int(d), int(m), int(y)))