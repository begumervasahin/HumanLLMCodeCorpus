b1 = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 0, 0, 67]
def fonk1(b1, x, i):
    if i <= len(b1):
        if b1[i-1] != 0:
            print("Checking", b1[i-1])
        if b1[i-1] == x:
            return i
        b2 = fonk1(b1, x, i*2)
        b3 = fonk1(b1, x, (i*2)+1)
        if b2 != -1:
            return b2
        if b3 != -1:
            return b3
        return -1
    else:
        return -1
def fonk2(b1, x, i):
    if i <= len(b1):
        b4 = []
        b5 = i
        for y in range(i):
            b4.append(b1[b5-1])
            if len(b1) > b5:
                b5 += 1
        for y in range(i):
            print("Checking", b4[y])
            if b4[y] == x:
                print("Yay,", x, "is found")
                return i
        print("Change row")
        for y in range(i):
            b4.pop()
        b6 = fonk2(b1, x, i*2)
        if b6 != -1:
            return b6
        return -1
    else:
        return -1
print("DFS:")
b7 = fonk1(b1, 72, 1)
if b7 != -1:
    print("Value found at index:", b7)
else:
    print("Value not found")
print("\nBFS:")
b8 = fonk2(b1, 72, 1)
if b8 != -1:
    print("Value found at index:", b8)
else:
    print("Value not found")