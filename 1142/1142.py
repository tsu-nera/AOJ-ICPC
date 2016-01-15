n = input()

for _ in range(n):
    s = raw_input()

    bag = set()
    for i in range(len(s)):
        head = s[:i]
        tail = s[i:]

        bag.add(head + tail)
        bag.add(head + tail[:: -1])
        bag.add(head[:: -1] + tail)
        bag.add(head[:: -1] + tail[:: -1])
        bag.add(tail + head)
        bag.add(tail + head[:: -1])
        bag.add(tail[:: -1] + head)
        bag.add(tail[:: -1] + head[:: -1])

    print len(bag)
