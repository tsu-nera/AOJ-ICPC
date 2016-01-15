while True:
    n = input()
    if n == 0:
        break
    W, H = map(int, raw_input().split())
    p = set()

    for _ in range(n):
        x, y = map(int, raw_input().split())
        p.add((x, y))

    S, T = map(int, raw_input().split())

    mcnt = 0
    for col in range(W - S + 1):
        for row in range(H - T + 1):
            cnt = 0
            for i in range(col, col + S):
                for j in range(row, row + T):
                    if (i + 1, j + 1) in p:
                        cnt += 1
            mcnt = max(mcnt, cnt)
    print mcnt
