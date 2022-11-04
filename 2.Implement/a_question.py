# 여행가 A는 N*N 크기의 정사각형 공간 위에 존재
# 시작 위치 1,1
# L, R, U, D 로 이동 명령을 받고 공간밖으로 이동하는 명령은 무시

def my_answer():
    n = int(input())
    # move_pattern = ['R', 'R', 'R', 'U', 'D', 'D'] # test case
    move_pattern = input().split()
    move_type = {'L': -1, 'R': 1, 'U': -1, 'D': 1}

    x, y = 1, 1

    for i in move_pattern:
        if i in ['R', 'L']:
            if y + move_type[i] != 0 and y + move_type[i] < n+1:
                y += move_type[i]
        elif i in ['U', 'D']:
            if x + move_type[i] != 0 and x + move_type[i] < n+1:
                x += move_type[i]

    print(x, y)


def model_answer():
    n = int(input())
    x, y = 1, 1

    move_pattern = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for move in move_pattern:
        for i in range(len(move_types)):
            if move == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

    print(x, y)
