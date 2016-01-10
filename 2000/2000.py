
moves = {"N": (0, 1),
         "S": (0, -1),
         "E": (1, 0),
         "W": ( -1, 0)}

while True:
    n = int(raw_input())

    if n == 0:
        break

    houseki = set()
    pos = (10, 10)

    for i in range(n):
        x, y = map(int, raw_input().split())
        houseki.add((x, y))

    m = int(raw_input())
    for j in range(m):
        d, cnt = raw_input().split()
        move = moves[d]

        for k in range(int(cnt)):
            pos = (pos[0] + move[0], pos[1] + move[1])

            if pos in houseki:
                houseki.remove(pos)

    if len(houseki) == 0:
        print "Yes"
    else:
        print "No"
