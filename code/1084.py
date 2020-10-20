# [기초-종합] 빛 섞어 색 만들기(설명)
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1084
'''
R, G, B = map(int, input().split())

for r in range(R):
    for g in range(G):
        for b in range(B):
            print(r, g, b)
print(R*G*B)