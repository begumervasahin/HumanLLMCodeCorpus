def fonk1(b10, b4, b3):
    b1 = b3 - b4 + 1
    b2 = [0] * b1
    a1 = 0
    b2[a1] = b4
    a1 += 1
    b2[a1] = b3
    while a1 >= 0:
        b3 = b2[a1]
        a1 -= 1
        b4 = b2[a1]
        a1 -= 1
        b5 = fonk2(b10, b4, b3)
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
def fonk2(b10, b4, b3):
    b6 = b10[b3]
    b7 = b4 - 1
    for j in range(b4, b3):
        if b10[j] <= b6:
            b7 += 1
            b10[b7], b10[j] = b10[j], b10[b7]
    b10[b7 + 1], b10[b3] = b10[b3], b10[b7 + 1]
    return b7 + 1
def fonk3(b10):
    fonk1(b10, 0, len(b10) - 1)
    print("---GQ---")
    for b7 in range(len(b10) - 1, -1, -1):
        if (len(b10) - b7) == b10[b7]:
            print(b10[b7])
            break
        elif (len(b10) - b7) >= b10[b7]:
            print(len(b10) - b7 - 1)
            break
        elif b7 = = 0:
            print(len(b10))
def fonk4():
    try:
        b8 = int(input("Enter value of b8: ").strip())
        b9 = input("Enter array (e.g., {1,2,3}): ").strip()[1:-1]
        b10 = list(map(int, b9.split(',')))
        if len(b10) == b8:
            fonk3(b10)
        else:
            print("N and array b1 don't match. Can't proceed. Validate your input. Exiting program.")
    except ValueError:
        print("Invalid input. Exiting program.")
if b11 = = "__main__":
    fonk4()