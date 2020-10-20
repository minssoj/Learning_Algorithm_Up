# [기초-종합] 소리 파일 저장용량 계산하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1085
'''
h, b, c, s = map(int, input().split())
print('{:.1f} MB'.format(h * b * c * s / (8 *(2 ** 20))))