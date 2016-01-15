n = input()
U = [raw_input() for _ in range(n)]
m = input()
T = [raw_input() for _ in range(m)]

isOpen = False

for t in T:
    if t in U:
        if isOpen:
            isOpen = False
            print "Closed by " + t
        else:
            isOpen = True
            print "Opened by " + t
    else:
        print "Unknown " + t
