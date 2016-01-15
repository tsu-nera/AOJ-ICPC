vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]


def isBound(n, m, x, y):
    return x < 0 or y < 0 or x >= n or y >= m


def dfs(x, y):
    global field
    global cnt
    global v

    if isBound(W, H, x, y):
        return
    if field[y][x] == '#':
        return
    if v[y][x]:
        return
    else:
        v[y][x] = True
        cnt += 1

    for i in range(4):
        nx = x + vx[i]
        ny = y + vy[i]
        dfs(nx, ny)

while True:
    W, H = map(int, raw_input().split())

    if W == 0:
        break

    field = []
    for h in range(H):
        field.append(raw_input())

    v = [[False for i in range(W)] for j in range(H)]

    cnt = 0
    for x in range(W):
        for y in range(H):
            if field[y][x] == '@':
                dfs(x, y)
    print cnt
