ref = {"1":".,!? ",
       "2":"abc",
       "3":"def",
       "4":"ghi",
       "5":"jkl",
       "6":"mno",
       "7":"pqrs",
       "8":"tuv",
       "9":"wxyz"}

n = int(raw_input())

for _ in range(n):
    ans = ""
    inputs = map(str, raw_input().split('0'))

    for i in inputs:
        if len(i) > 0:
            k = i[0]
            ans += ref[k][(len(i) - 1) % len(ref[k])]
    print ans
