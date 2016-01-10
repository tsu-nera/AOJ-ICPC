while True:
    n = int(raw_input())

    if n == 0:
        break

    cnt = 0

    for i in range(1, n):
        temp = 0
        for j in range(i, n):
            temp += j
            if temp == n:
                cnt += 1
            elif temp > n:
                break
    print cnt
