def fonk1(b5, b6):
    b1 = sorted([b5, b6])
    b2 = []
    for num in range(b1[0] + 1, b1[1]):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            b2.append(num)
    return b2
def fonk2(b2):
    b3 = b2[:]
    for i in range(0, len(b3) - 1, 3):
        b3[i] = str(b3[i]) + ":"
    for i in range(1, len(b3) - 1, 3):
        b3[i] = str(b3[i]) + "!"
    for i in range(2, len(b3) - 1, 3):
        b3[i] = str(b3[i]) + ","
    return b3
if b4 = = "__main__":
    b5 = int(input("Enter the first number: "))
    b6 = int(input("Enter the second number: "))
    b2 = fonk1(b5, b6)
    if b2:
        b3 = fonk2(b2)
        print("".join(map(str, b3)))
    else:
        print("No prime numbers found")