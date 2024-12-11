def fonk1(b4, b1 = 0, desc=0):
    b2 = max(b4)
    b3 = min(b4)
    if b3:
        b4 = [x - b3 for x in b4]
    if b1:
        print("Normalized list:", b4)
    b5 = [0] * (b2 - b3 + 1)
    for num in b4:
        b5[num] += 1
    for i in range(1, len(b5)):
        b5[i] += b5[i - 1]
        if b1 = = 2:
            print("Cumulative b5:", i, "::", b5[i])
    b6 = len(b4)
    b7 = [0] * b6
    for i in range(b6 - 1, -1, -1):
        b5[b4[i]] -= 1
        b7[b5[b4[i]]] = b4[i]
        if b1:
            print("Iteration", i, ":", b7)
    if b3:
        b7 = [x + b3 for x in b7]
    if desc:
        b7 = b7[::-1]
    return b7