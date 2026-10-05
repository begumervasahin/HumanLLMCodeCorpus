b1 = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 0, 0, 67]
def fonk1(b1, target, index):
    if index <= len(b1):
        b2 = b1[index - 1]
        if b2 != 0:
            print("Checking", b2)
        if b2 = = target:
            return index
        b3 = fonk1(b1, target, index * 2)
        if b3 != -1:
            return b3
        b4 = fonk1(b1, target, (index * 2) + 1)
        if b4 != -1:
            return b4
        return -1
    else:
        return -1
def fonk2(b1, target, index):
    if index <= len(b1):
        b5 = []
        b6 = index
        for _ in range(index):
            b5.append(b1[b6 - 1])
            if len(b1) > b6:
                b6 += 1
        for _ in range(index):
            print("Checking", b5[_])
            if b5[_] == target:
                print("Yay,", target, "is found")
                return index
        print("Change row")
        for _ in range(index):
            b5.pop()
        b7 = fonk2(b1, target, index * 2)
        if b7 != -1:
            return b7
        return -1
    else:
        return -1
print("DFS:")
b8 = fonk1(b1, 72, 1)
if b8 != -1:
    print("Value found at index:", b8)
else:
    print("Value not found")
print("\nBFS:")
b9 = fonk2(b1, 72, 1)
if b9 != -1:
    print("Value found at index:", b9)
else:
    print("Value not found")