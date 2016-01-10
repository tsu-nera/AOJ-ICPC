for _ in range(input()):
    asset = ans = input()
    year = input()
    n = input()
    for i in range(n):
        plan, rate, cost = map(float, raw_input().split())
        if plan == 0.0:
            rates = sum(int(rate * (asset - y * cost)) for y in range(year))
            ans = max(ans, rates + asset - year*cost)
        else:
            cur = asset
            for y in range(year):
                cur = int(cur * (1 + rate) - cost)
            ans = max(ans, cur)
    print int(ans)
