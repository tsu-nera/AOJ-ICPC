n = int(input())


def mcxi2int(s):
    m = {'m': 1000, 'c': 100, 'x': 10, 'i': 1}

    ret = 0
    i = 0
    while i < (len(s)):
        num = 1
        maci = s[i]
        if maci.isdigit():
            num = int(maci)
            maci = s[i + 1]
            i += 1
        ret += num * m[maci]
        i += 1
    return ret


def int2mcxi(n):
    keys = ['m', 'c', 'x', 'i']
    values = [1000, 100, 10, 1]

    ret = ""
    for k, v in zip(keys, values):
        i = n / v
        n = n % v
        if i == 0:
            continue
        elif i == 1:
            ret = ret + k
        else:
            ret = ret + str(i) + k
    return ret

for _ in range(n):
    m1, m2 = raw_input().split()
    print int2mcxi(mcxi2int(m1) + mcxi2int(m2))
