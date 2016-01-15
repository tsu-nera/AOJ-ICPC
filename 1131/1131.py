global p, q, a


def dfs(n, d, prod, total):
    cnt = 0

    i = d
    while prod * i <= a:
        left = p * (prod * i)
        right = total * i + prod

        if left < right * q:
            i += 1
            continue
        if left == right * q:
            cnt += 1
            i += 1
            continue
        if n == 1:
            i += 1
            continue
        cnt += dfs(n - 1, i, prod * i, right)
        i += 1
    return cnt

while True:
    p, q, a, n = map(int, raw_input().split())

    if p == 0:
        break

    print dfs(n, 1, 1, 0)
