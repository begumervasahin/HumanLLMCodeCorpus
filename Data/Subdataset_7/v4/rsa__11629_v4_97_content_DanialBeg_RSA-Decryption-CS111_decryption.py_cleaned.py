import string
def fonk1(a, b):
    for num in range(1, b):
        if ((a * num) % b) == 1:
            return num
    return 1
def fonk2(r):
    b1 = []
    a1 = 1
    while a1 <= r:
        if r % a1 = = 0:
            b1.append(a1)
        a1 += 1
    return b1
def fonk3():
    b2 = int(input("Please enter the exponent value in the public key: "))
    b3 = int(input("Please enter the b3 value in the public key: "))
    print("Public key values: ", b2, b3)
    b4 = fonk2(b3)
    b5 = b4[1]
    b6 = b4[2]
    b7 = (b5 + 1) * (b6 + 1)
    b8 = fonk1(b2, b7)
    b9 = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
                  27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
                  25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
                  7, 25, 10, 49, 18, 52, 51, 39]
    b10 = list(string.ascii_lowercase)
    b10.append(' ')
    for a1 in b9:
        b11 = (a1 ** b8) % b3
        print(str(b10[b11 - 2]), b12 = "")
if b13 = = "__main__":
    fonk3()