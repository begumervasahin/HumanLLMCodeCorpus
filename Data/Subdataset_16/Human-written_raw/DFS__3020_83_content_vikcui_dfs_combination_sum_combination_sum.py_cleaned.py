
def fonk1(inputList, target):
    inputList.sort()
    b1 = []
    a1 = 0
    b2 = []
    fonk2(inputList, target, a1, b2, b1)
    return b1
def fonk2(inputList, target, a1, b2, b1):
    for j in range(a1, len(inputList)):
        b3 = inputList[j]
        if b3 > target:
            return
        b2.append(b3)
        if b3 < target:
            fonk2(inputList, target - b3, j, b2, b1)
        else:
            b1.append(list(b2))
        b2.pop()
    return