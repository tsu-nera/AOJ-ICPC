def is_same(A, B):
    for row in range(2):
        for i in range(4):
            if A == B:
                return True
        B = [[y, x] for x, y in B]
    B = [[x - B[-1][0], y - B[-1][-1]] for x, y in B][::-1]
    return False

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
