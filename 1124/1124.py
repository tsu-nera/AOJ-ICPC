while True:
    n, q = map(int, raw_input().split())

    if n == 0:
        break

    m = {}

    for _ in range(n):
        d = map(int, raw_input().split())
        for i in range(1, len(d)):
            if d[i] in m:
                m[d[i]] += 1
            else:
                m[d[i]] = 1

    maxk = 0
    maxv = 0
    for k, v in m.items():
        if v >= q and maxv < v:
            maxk = k
            maxv = v

    print maxk
