def fonk1(b10, b3, b2):
    b1 = [0] * (b2 - b3 + 1)
    a1 = 0
    b1[a1] = b3
    a1 += 1
    b1[a1] = b2
    while a1 >= 0:
        b2 = b1[a1]
        a1 -= 1
        b3 = b1[a1]
        a1 -= 1
        b4 = fonk2(b10, b3, b2)
        if b4 - 1 > b3:
            a1 += 1
            b1[a1] = b3
            a1 += 1
            b1[a1] = b4 - 1
        if b4 + 1 < b2:
            a1 += 1
            b1[a1] = b4 + 1
            a1 += 1
            b1[a1] = b2
def fonk2(b10, b3, b2):
    b5 = b10[b2]
    b6 = b3 - 1
    for j in range(b3, b2):
        if b10[j] <= b5:
            b6 += 1
            b10[b6], b10[j] = b10[j], b10[b6]
    b10[b6 + 1], b10[b2] = b10[b2], b10[b6 + 1]
    return b6 + 1
def fonk3(b10):
    fonk1(b10, 0, len(b10) - 1)
    print("---GQ---")
    for b6 in range(len(b10) - 1, -1, -1):
        b7 = len(b10) - b6
        if b7 = = b10[b6]:
            print(b10[b6])
            break
        elif b7 >= b10[b6]:
            print(b7 - 1)
            break
        elif b6 = = 0:
            print(len(b10))
def fonk4():
    try:
        b8 = int(input("Enter value of b8: ").strip())
        b9 = input("Enter array (e.g., {1,2,3}): ").strip()[1:-1]
        b10 = list(map(int, b9.split(',')))
        if len(b10) == b8:
            fonk3(b10)
        else:
            print("N and array size don't match. Can't proceed. Validate your input. Exiting program.")
    except ValueError:
        print("Invalid input. Exiting program.")
if b11 = = "__main__":
    fonk4()