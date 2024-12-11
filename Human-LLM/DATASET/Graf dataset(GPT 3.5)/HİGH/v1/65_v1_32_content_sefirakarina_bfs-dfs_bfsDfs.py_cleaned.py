b1 = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 0, 0, 67]
def fonk1(b1, x, i):
    if i <= len(b1):
        if b1[i-1] != 0:
            print("Checking", b1[i-1])
        if b1[i-1] == x:
            return i
        b2 = fonk1(b1, x, i*2)
        if b2 != -1:
            return b2
        b2 = fonk1(b1, x, (i*2)+1)
        if b2 != -1:
            return b2
        return -1
    else:
        return -1
def fonk2(b1, x, i):
    if i <= len(b1):
        b3 = []
        b4 = i
        for y in range(i):
            b3.append(b1[b4-1])
            if len(b1) > b4:
                b4 += 1
        for y in range(i):
            print("Checking", b3[y])
            if b3[y] == x:
                print("Yay,", x, "is found")
                return i
        print("Change row")
        for y in range(i):
            b3.pop()
        b2 = fonk2(b1, x, i*2)
        if b2 != -1:
            return b2
        return -1
    else:
        return -1
print("DFS:")
b5 = fonk1(b1, 72, 1)
if b5 != -1:
    print("Value found at index:", b5)
else:
    print("Value not found")
print("\nBFS:")
b6 = fonk2(b1, 72, 1)
if b6 != -1:
    print("Value found at index:", b6)
else:
    print("Value not found")