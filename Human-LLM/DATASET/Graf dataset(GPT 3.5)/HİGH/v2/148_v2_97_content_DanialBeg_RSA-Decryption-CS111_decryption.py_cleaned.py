import string
def fonk1():
    b1 = int(input("Please enter the b1 value in the public key: "))
    b2 = int(input("Please enter the b2 value in the public key: "))
    print("Exponent:", b1)
    print("Modulus:", b2)
    p, b3 = fonk2(b2)
    b4 = (p + 1) * (b3 + 1)
    b5 = fonk3(b1, b4)
    b6 = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
                   27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
                   25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
                   7, 25, 10, 49, 18, 52, 51, 39]
    b7 = list(string.ascii_lowercase)
    b7.append(' ')
    b8 = fonk4(b6, b5, b2, b7)
    print("Decrypted Message:", b8)
def fonk2(number):
    b9 = []
    for b10 in range(1, number + 1):
        if number % b10 = = 0:
            b9.append(b10)
    return b9[1], b9[2]
def fonk3(a, b11):
    for num in range(1, b11):
        if (a * num) % b11 = = 1:
            return num
    return 1
def fonk4(b6, b5, b2, b7):
    b8 = ""
    for encrypted_char in b6:
        b12 = pow(encrypted_char, b5, b2) - 2
        b13 = b7[b12]
        b8 += b13
    return b8
if b14 = = "__main__":
    fonk1()