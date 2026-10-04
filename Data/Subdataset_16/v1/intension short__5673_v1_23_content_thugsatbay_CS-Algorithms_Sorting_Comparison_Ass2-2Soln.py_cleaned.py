def fonk1(b9, b4, b3):
    b1 = b3 - b4 + 1
    b2 = [0] * b1
    a1 = -1
    a1 += 1
    b2[a1] = b4
    a1 += 1
    b2[a1] = b3
    while a1 >= 0:
        b3 = b2[a1]
        a1 -= 1
        b4 = b2[a1]
        a1 -= 1
        b5 = b4 - 1
        b6 = b9[b3]
        for j in range(b4, b3):
            if b9[j] <= b6:
                b5 += 1
                b9[b5], b9[j] = b9[j, b9[b5]]
        b9[b5 + 1], b9[b3] = b9[b3, b9[b5 + 1]]
        b5 += 1
        if abs(b4 - b5) < abs(b3 - b5):
            if b5 + 1 < b3:
                a1 += 1
                b2[a1] = b5 + 1
                a1 += 1
                b2[a1] = b3
            if b5 - 1 > b4:
                a1 += 1
                b2[a1] = b4
                a1 += 1
                b2[a1] = b5 - 1
        else:
            if b5 - 1 > b4:
                a1 += 1
                b2[a1] = b4
                a1 += 1
                b2[a1] = b5 - 1
            if b5 + 1 < b3:
                a1 += 1
                b2[a1] = b5 + 1
                a1 += 1
                b2[a1] = b3
def fonk2(b9):
    fonk1(b9, 0, len(b9) - 1)
    print("---GQ---")
    for b7 in range(len(b9) - 1, -1, -1):
        if len(b9) - b7 = = b9[b7]:
            print(b9[b7])
            break
        elif len(b9) - b7 >= b9[b7]:
            print(len(b9) - b7 - 1)
            break
        elif b7 = = 0:
            print(len(b9))
def fonk3():
    b8 = int(input("Enter value of b8: ").strip())
    b9 = list(map(int, input("Enter array: [Example: {1,2,3}]: ").strip()[1:-1].split(',')))
    if len(b9) == b8:
        fonk2(b9)
    else:
        print("N and array b1 don't match, can't proceed. Validate your input. Exiting Program.")
if b10 = = "__main__":
    fonk3()