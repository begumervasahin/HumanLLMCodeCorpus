def fonk1(qPArr, b4, b3):
    b1 = b3 - b4 + 1
    b2 = [0] * b1
    a1 = -1
    a1 = a1 + 1
    b2[a1] = b4
    a1 = a1 + 1
    b2[a1] = b3
    while a1 >= 0:
        b3 = b2[a1]
        a1 = a1 - 1
        b4 = b2[a1]
        a1 = a1 - 1
        b5 = b4 - 1
        b6 = qPArr[b3]
        for j in range(b4, b3):
            if qPArr[j] <= b6:
                b5 = b5 + 1
                qPArr[b5], qPArr[j] = qPArr[j], qPArr[b5]
        qPArr[b5 + 1], qPArr[b3] = qPArr[b3], qPArr[b5 + 1]
        b6 = b5 + 1
        if abs(b4 - b6) < abs(b6 - b3):
            if b6 + 1 < b3:
                a1 = a1 + 1
                b2[a1] = b6 + 1
                a1 = a1 + 1
                b2[a1] = b3
            if b6 - 1 > b4:
                a1 = a1 + 1
                b2[a1] = b4
                a1 = a1 + 1
                b2[a1] = b6 - 1
        else:
            if b6 - 1 > b4:
                a1 = a1 + 1
                b2[a1] = b4
                a1 = a1 + 1
                b2[a1] = b6 - 1
            if b6 + 1 < b3:
                a1 = a1 + 1
                b2[a1] = b6 + 1
                a1 = a1 + 1
                b2[a1] = b3
def fonk2(arrGQ):
    fonk1(arrGQ, 0, len(arrGQ) - 1)
    print("---GQ---")
    for b7 in range(len(arrGQ) - 1, -1, -1):
        if len(arrGQ) - b7 = = arrGQ[b7]:
            print(arrGQ[b7])
            break
        elif len(arrGQ) - b7 >= arrGQ[b7]:
            print(len(arrGQ) - b7 - 1)
            break
        elif b7 = = 0:
            print(len(arrGQ))
def fonk3():
    print("Enter value Of b8:")
    b8 = int(input().strip())
    print("Enter array in format [1, 2, 3]:")
    b9 = list(map(int, input().strip()[1:-1].strip().split(',')))
    if len(b9) == b8:
        fonk2(b9)
    else:
        print("Error: N and array b1 don't match. Exiting Program.")
if b10 = = "__main__":
    fonk3()