import sys
def fonk1(qPArr, b4, b3):
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
        b6 = qPArr[b3]
        for j in range(b4, b3):
            if qPArr[j] <= b6:
                b5 += 1
                qPArr[b5], qPArr[j] = qPArr[j], qPArr[b5]
        qPArr[b5 + 1], qPArr[b3] = qPArr[b3], qPArr[b5 + 1]
        b5 = b5 + 1
        if abs(b4 - b5) < abs(b5 - b3):
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
def fonk2(b11):
    fonk1(b11, 0, len(b11) - 1)
    print("---GQ---")
    for b7 in range(len(b11) - 1, -1, -1):
        if len(b11) - b7 = = b11[b7]:
            print(b11[b7])
            break
        elif len(b11) - b7 >= b11[b7]:
            print(len(b11) - b7 - 1)
            break
        elif b7 = = 0:
            print(len(b11))
def fonk3(prompt):
    while True:
        try:
            b8 = int(input(prompt).strip())
            return b8
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def fonk4():
    print("Enter the b8 of b9:")
    b9 = fonk3()
    print("Enter the array in the format [1, 2, 3]:")
    b10 = input().strip()
    b11 = list(map(int, b10[1:-1].split(',')))
    if len(b11) == b9:
        fonk2(b11)
    else:
        print("Error: N and array b1 don't match. Exiting Program.")
if b12 = = "__main__":
    fonk4()