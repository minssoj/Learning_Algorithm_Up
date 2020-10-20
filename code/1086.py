# [기초-종합] 그림 파일 저장용량 계산하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1086
'''
w, h, b = map(int, input().split())
print('{:.2f} MB'.format(w * h * b/ (8 *(2 ** 20))))