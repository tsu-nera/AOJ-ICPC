dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cnt):
    global board, W, H, ans
    if cnt >= ans:
        return

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if 0 > mx or 0 > my or W <= mx or H <= my:
            continue
        if board[my][mx] == 1:
            continue

        while True:
            if board[my][mx] == 3:
                ans = cnt
                return

            mx += dx[i]
            my += dy[i]

            if 0 > mx or 0 > my or W <= mx or H <= my:
                break

            if board[my][mx] == 1:
                board[my][mx] = 0
                dfs(mx - dx[i], my - dy[i], cnt + 1)
                board[my][mx] = 1
                break

while True:
    W, H = map(int, raw_input().split())
    if W == 0:
        break

    ans = 11
    board = [map(int, raw_input().split()) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if board[y][x] == 2:
                sx, sy = x, y
    dfs(sx, sy, 1)
    print ans if ans < 11 else - 1
