while True:
    n, p = map(int, raw_input().split())
    if n == 0:
        break

    cnt = [0] * n
    wan = p
    pos = 0

    while True:
        if wan:
            cnt[pos] += 1
            wan -= 1

            if wan == 0 and cnt[pos] == p:
                print pos
                break
        else:
            wan = cnt[pos]
            cnt[pos] = 0
        pos = (pos + 1) % n
