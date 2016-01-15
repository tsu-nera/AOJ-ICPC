def tax(a, p):
    return int(a * (100 + p) / 100.0)

while True:
    x, y, s = map(int, raw_input().split())

    if x == 0:
        break

    results = []

    for i in range(1, s):
        for j in range(1, s - i + 1):
            if tax(i, x) + tax(j, x) != s:
                continue
            results.append(tax(i, y) + tax(j, y))

    if len(results) == 0:
        print 0
    else:
        print max(results)
