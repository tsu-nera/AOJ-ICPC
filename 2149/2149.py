while True:
    N, A, B, C, X = map(int, raw_input().split())

    if N == 0:
        break

    Y = map(int, raw_input().split())
    cnt = -1
    i = 0

    while i < len(Y):
        if Y[i] == X:
            i += 1
        if cnt == 10000:
            cnt = -1
            break
        X = (A * X + B) % C
        cnt += 1

    print cnt
