import common as c
def fonk1(b8, b1 = 0, desc=0):
    def fonk2(number, b2):
        a1 = 0
        while number:
            a1 += 1
            number
        return a1
    def fonk3(number, position, b2 = 10):
        a1 = 0
        while True:
            a1 += 1
            b3 = number % b2
            number
            if a1 > position:
                break
        return b3
    def fonk4(position, b2):
        b4 = len(b8)
        b5 = [[] for _ in range(b4)]
        for i in range(b4):
            b6 = fonk3(b8[i], position, b2)
            b5[b6].append(b8[i])
            if b1 = = 2:
                print("    Bucket:", i, " :: ", b5)
        return [b5[x][y] for x in range(len(b5)) for y in range(len(b5[x]))]
    b2 = 10
    b7 = c.minimum(b8)[0]
    if b7:
        b8 = [x - b7 for x in b8]
    b9 = c.maximum(b8)[0]
    b10 = fonk2(b9, b2)
    for i in range(b10):
        b8 = fonk4(i, b2)
        if b1:
            print("Iteration", i + 1, ":", b8)
    if b7:
        b8 = [x + b7 for x in b8]
    if desc:
        b8 = b8[::-1]
    return b8
if b11 = = "__main__":
    b12 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", b12)
    b13 = fonk1(b12, b1=1, desc=0)
    print("Sorted Array:", b13)