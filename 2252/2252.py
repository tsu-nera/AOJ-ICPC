left = "qwertasdfgzxcvb"

while True:
    s = raw_input()
    if s == "#":
        break
    cnt = 0

    if s[0] in left:
        isleft = True
    else:
        isleft = False

    for i in range(1, len(s)):
        if s[i] in left:
            if not isleft:
                cnt += 1
            isleft = True
        else:
            if isleft:
                cnt += 1
            isleft = False

    print cnt
