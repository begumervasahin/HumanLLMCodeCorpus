import string
def fonk1():
    b8, b1 = fonk2()
    print("Exponent:", b8)
    print("Modulus:", b1)
    p, b2 = fonk3(b1)
    b3 = fonk4(p, b2)
    b4 = fonk5(b8, b3)
    b5 = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
                   27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
                   25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
                   7, 25, 10, 49, 18, 52, 51, 39]
    b6 = list(string.ascii_lowercase)
    b6.append(' ')
    b7 = fonk7(b5, b4, b1, b6)
    print("Decrypted Message:", b7)
def fonk2():
    b8 = int(input("Please enter the b8 value in the public key: "))
    b1 = int(input("Please enter the b1 value in the public key: "))
    return b8, b1
def fonk3(number):
    b9 = []
    for b10 in range(1, number + 1):
        if number % b10 = = 0:
            b9.append(b10)
    return b9[1], b9[2]
def fonk4(p, b2):
    return (p + 1) * (b2 + 1)
def fonk5(b8, b3):
    return fonk6(b8, b3)
def fonk6(a, b11):
    for num in range(1, b11):
        if (a * num) % b11 = = 1:
            return num
    return 1
def fonk7(b5, b4, b1, b6):
    b7 = ""
    for encrypted_char in b5:
        b12 = pow(encrypted_char, b4, b1) - 2
        b13 = b6[b12]
        b7 += b13
    return b7
if b14 = = "__main__":
    fonk1()