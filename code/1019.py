# [기초-입출력] 연월일 입력받아 그대로 출력하기
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1019
'''
y, m, d = input().split('.')
print('{:04d}.{:02d}.{:02d}'.format(int(y), int(m), int(d)))