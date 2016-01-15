while True:
    n, m, p = map(int, raw_input().split())
    if n == 0:
        break
    x = [int(raw_input()) for _ in range(n)]

    if x[m - 1] == 0:
        print 0
    else:
        print sum(x)*(100 - p) / x[m - 1]
