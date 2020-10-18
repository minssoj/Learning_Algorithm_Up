# [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1071
* 반복문 없이 문제풀이 -> 함수 이용
'''

n = list(map(int, input().split()))

def f(index):
    if n[index] != 0:
        print(n[index])
        f(index+1)

f(0)
