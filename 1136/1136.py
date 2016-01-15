def is_same(A, B):
    pass

while 1:
    n = int(raw_input())
    if n == 0:
        break
    poly = []
    for i in range(n + 1):
        m = int(raw_input())
        xy = [map(int, raw_input().split()) for _ in range(m)]
        poly.append([x - xy[0][0], y - xy[0][0]] for x, y in xy)
    for i in range(1, n + 1):
        if is_same(poly[0], poly[i]):
            print i
    print "+++++"
