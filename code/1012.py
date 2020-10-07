# [기초-입출력] 실수 1개 입력받아 그대로 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1012
'''
f = float(input())
# print(f)
print('{:.6f}'.format(f))   # 입력 : 1.54인경우, 출력 : 1.540000 을 위해...