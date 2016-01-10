while True:
    n, m = map(int, raw_input().split())

    if n == 0:
        break

    taro = [int(raw_input()) for i in range(n)]
    taro_sum = sum(taro)
    hanako = [int(raw_input()) for j in range(m)]
    hanako_sum = sum(hanako)

    pair = (101, 101)

    for t in taro:
        for h in hanako:
            if taro_sum - t + h == hanako_sum - h + t:
                if h + t <= sum(pair):
                    pair = (t, h)

    if pair == (101, 101):
        print - 1
    else:
        print pair[0], pair[1]
