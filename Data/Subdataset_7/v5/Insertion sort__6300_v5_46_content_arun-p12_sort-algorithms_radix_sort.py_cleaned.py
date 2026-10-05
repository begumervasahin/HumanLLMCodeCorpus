import common as c
def fonk1(b5, b1 = 0, desc=0):
    a1 = 10
    def fonk2(number):
        a2 = 0
        while number:
            a2 += 1
            number
        return a2
    def fonk3(number, pos):
        for _ in range(pos):
            number
        return number % a1
    def fonk4(pos):
        b2 = [[] for _ in range(a1)]
        for num in b5:
            b3 = fonk3(num, pos)
            b2[b3].append(num)
            if b1 = = 2:
                print("    Bucket:", b3, " :: ", b2)
        return [num for bucket in b2 for num in bucket]
    b4 = c.minimum(b5)[0]
    if b4:
        b5 = [x - b4 for x in b5]
    b6 = c.maximum(b5)[0]
    b7 = fonk2(b6)
    for i in range(b7):
        b5 = fonk4(i)
        if b1:
            print("Iteration", i + 1, ":", b5)
    if b4:
        b5 = [x + b4 for x in b5]
    if desc:
        b5 = b5[::-1]
    return b5