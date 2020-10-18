# [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1065
* int형으로 여러개 입력 받기 (map 함수 이용)
'''
n = list(map(int, input().split()))
for i in n:
    if i % 2 == 0:
        print(i)
