cnt = 0
while True:
    n = input()

    if n == 0:
        break

    if cnt > 0:
        print

    y10, y50, y100, y500 = map(int, raw_input().split())
    Sum = 10 * y10 + 50 * y50 + y100 * 100 + y500 * 500

    while Sum - 500 >= n:
        Sum -= 500
        y500 -= 1
    while Sum - 100 >= n:
        Sum -= 100
        y100 -= 1
    while Sum - 50 >= n:
        Sum -= 50
        y50 -= 1
    while Sum - 10 >= n:
        Sum -= 10
        y10 -= 1

    if y10 > 0:
        print 10, y10
    if y50 > 0:
        print 50, y50
    if y100 > 0:
        print 100, y100
    if y500 > 0:
        print 500, y500

    cnt += 1
