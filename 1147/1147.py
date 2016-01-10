while True:
    n = int(input())
    if n == 0:
        break

    ma = 0
    mi = 1000
    s = 0

    for i in range(n):
        x = int(input())
        if ma < x:
            ma = x
        if mi > x:
            mi = x
        s += x

    print ((s - ma - mi) // (n - 2))
