import math

def dist(x, y):
    return math.sqrt(x * x + y * y)

def solve(t, x, y):
    global n, dx, dy, answer
    global done, cx, cy

    if answer:
        return

    collected = 0
    for i in range(n):
        if done[i]:
            collected += 1

    if collected == n:
        answer = True
        return

    for i in range(n):
        if done[i]:
            continue
        nt = t + dist(cx[i] - x, cy[i] - y)
        if dist(dx - cx[i], dy - cy[i]) < nt + 0.00000000001:
            return

    for i in range(n):
        if done[i]:
            continue

        done[i] = True
        nt = t + dist(cx[i] - x, cy[i] - y)
        solve(nt, cx[i], cy[i])
        done[i] = False

n, hx, hy, dx, dy = map(int, raw_input().split())

cx = []
cy = []

for _ in range(n):
    x, y = map(int, raw_input().split())
    cx.append(x)
    cy.append(y)

done = [False for _ in range(20)]

answer = False
solve(0.0, hx, hy)

if answer:
    print "YES"
else:
    print "NO"
