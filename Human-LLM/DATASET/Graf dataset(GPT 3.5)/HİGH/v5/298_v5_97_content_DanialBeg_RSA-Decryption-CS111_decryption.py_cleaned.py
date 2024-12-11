import string
def fonk1(a, b1):
    for num in range(1, b1):
        if (a * num) % b1 = = 1:
            return num
    return 1
def fonk2(number):
    b2 = []
    for b3 in range(1, number + 1):
        if number % b3 = = 0:
            b2.append(b3)
    return b2
def fonk3():
    print("RSA Decryption Program\n")
    b4 = int(input("Please enter the b4 value in the public key: "))
    b5 = int(input("Please enter the n value in the public key: "))
    print("Public key values: ", b4, b5)
    b2 = fonk2(b5)
    b6 = b2[1]
    b7 = b2[2]
    b8 = (b6 + 1) * (b7 + 1)
    b9 = fonk1(b4, b8)
    b10 = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
                         27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
                         25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
                         7, 25, 10, 49, 18, 52, 51, 39]
    b11 = list(string.ascii_lowercase)
    b11.append(' ')
    b12 = ""
    for value in b10:
        b13 = (value ** b9) % b5
        b12 += b11[b13 - 2]
    print("\nDecrypted message:", b12)
if b14 = = "__main__":
    fonk3()