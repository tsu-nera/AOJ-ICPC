n = input()

for i in range(n):
    maxL = 0
    cx = 0
    cy = 0
    maxx = 0
    maxy = 0

    while True:
        dx, dy = map(int, raw_input().split())
        if dx == 0 and dy == 0:
            break
        cx += dx
        cy += dy
        d = cx ** 2 + cy ** 2
        if maxL < d or (d == maxL and cx > maxx):
            maxL = d
            maxx, maxy = cx, cy

    print maxx, maxy
