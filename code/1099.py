# [기초-2차원배열] 성실한 개미
# minso.jeong@daum.net
'''
문제링크 : https://www.codeup.kr/problem.php?id=1099
'''
# 입력
m = [list(map(int, input().split())) for _ in range(10)]
# 변수 선언
cx = 1  # 개미굴 현재위치 (2-1)
cy = 1  # 개미굴 현재위치 (2-1)
nx = 1  # 개미굴 다음위치
ny = 1  # 개미굴 다음위치
d = 0   # 오른쪽 :0, 아래쪽 :1

while True:
    while True:
        if m[cy][cx] == 2:
            break
        m[cy][cx] = 9
        ny = (1 * d) + cy
        nx = (1 * (1 - d)) + cx
        # print(cy, cx, ny, nx, d)

        if m[ny][nx] == 1:      # 장애물을 만나는 경우 방향 변경
            # print('방향변경')
            d = int(not(d))
            break
        elif m[cy][cx+1] == 0 and d==1:
            # print('방향오른쪽으로변경')
            nx += 1
            cx += 1
            d = 0
            break
        elif m[ny][nx] == 0:
            # print('정상')
            cy = ny
            cx = nx
        else:
            break
    if m[cy][cx] == 2:
        m[cy][cx] = 9
        break
    if (cy == 8 and cx == 8):
        break

    if m[ny][nx] == 2:
        m[ny][nx] = 9
        break

# 결과 출력
for j in range(10):
    for i in range(10):
        print(m[j][i], end=' ')
    print()



