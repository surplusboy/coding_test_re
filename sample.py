
# n = 4
# result = 	[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
def solotion(n:int):
    # result = [[0 for _ in range(n)] for _ in range(n)]
    result = [[0] * n for _ in range(n)]
    print(result)
    # print(result2)
    exit()
    x = 0
    y = 0
    num = 1
    for i in range(n):
        for j in range(n):
            result[x][y] = num
            num += 1
            y += 1
        y -= 1
        x += 1
        for k in range(n-1):
            result[x][y] = num
            num += 1
            x += 1
        x -= 1
        y -= 1
        for l in range(n-1):
            result[x][y] = num
            num += 1
            y -= 1
        y += 1
        x -= 1
        for m in range(n-2):
            result[x][y] = num
            num += 1
            x -= 1
        x += 1
        y += 1
        n -= 2
    return result

def solotion(n:int):
    spiral_list = [[0] * n for _ in range(n)]

    # limit point
    left = 0
    right = n - 1
    up = 1  # i == 0 부터 순회 하므로 up의 초기 값은 1이 된다.
    down = n - 1

    # 0: right, 1:down, 2:left, 3:up
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0  # initialize to right

    count = 1
    i = 0
    j = 0


    while count <= n * n:
        print(spiral_list)
        spiral_list[i][j] = count
        count += 1
        print(j, right)
        if direction % 4 == 0 and j == right:
            direction += 1
            right -= 1
        elif direction % 4 == 1 and i == down:
            direction += 1
            down -= 1
        elif direction % 4 == 2 and j == left:
            direction += 1
            left += 1
        elif direction % 4 == 3 and i == up:
            direction += 1
            up += 1
        # 다음 방문할 리스트 인덱스 설정
        i += di[direction % 4]
        j += dj[direction % 4]
    return spiral_list

print(solotion(6))
