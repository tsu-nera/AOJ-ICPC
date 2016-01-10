while True:
    n, r = map(int, raw_input().split())
    if n == 0 and r == 0:
        break

    l = range(n, 0, -1)

    for i in range(r):
        tmp = []
        p, c = map(int, raw_input().split())
        for j in range(c):
            tmp.append(l.pop(p - 1))
        l = tmp + l
    print l[0]
