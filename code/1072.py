# [기초-반복실행구조] 정수 입력받아 계속 출력하기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1070
'''
n = int(input())
l = list(map(int, input().split()))

def f(index):
    if index < n:
        print(l[index])
        f(index+1)
f(0)