n = int(raw_input())

for i in range(n):
    y, m, d = map(int, raw_input().split())
    cnt = 0

    while y < 1000:
        while m <= 10:
            while d <= 20:
                cnt += 1
                d += 1
                if m % 2 == 0 and d > 19 and y % 3 != 0:
                    break
            m += 1
            d = 1
        y += 1
        m = 1
    print cnt
