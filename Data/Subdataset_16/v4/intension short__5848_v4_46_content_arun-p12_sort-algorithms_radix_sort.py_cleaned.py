def fonk1(b6, b1 = 0, desc=0):
    def fonk2(n, b2):
        a1 = 0
        while n > 0:
            a1 += 1
            n
        return a1
    def fonk3(n, position, b2 = 10):
        for _ in range(position - 1):
            n
        return n % b2
    def fonk4(b6, position, b2):
        b3 = [[] for _ in range(b2)]
        for num in b6:
            b4 = fonk3(num, position, b2)
            b3[b4].append(num)
            if b1 = = 2:
                print(f"Bucket distribution for b4 position {position}: {b3}")
        return [num for bucket in b3 for num in bucket]
    b2 = 10
    b5 = min(b6)
    if b5 < 0:
        b6 = [x - b5 for x in b6]
    b7 = max(b6)
    b8 = fonk2(b7, b2)
    for i in range(1, b8 + 1):
        b6 = fonk4(b6, i, b2)
        if b1:
            print(f"After pass {i}: {b6}")
    if b5 < 0:
        b6 = [x + b5 for x in b6]
    if desc:
        b6.reverse()
    return b6