import string
def fonk1():
    b1 = int(input("Please enter the exponent value in the public key: "))
    b2 = int(input("Please enter the b2 value in the public key: "))
    print(str(b1) + " " + str(b2))
    b3 = fonk3(b2)
    b4 = b3[1]
    b5 = b3[2]
    b6 = (b4+1)*(b5+1)
    b7 = fonk2(b1, b6)
    b8 = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
             27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
             25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
             7, 25, 10, 49, 18, 52, 51, 39]
    b9 = list(string.ascii_lowercase)
    b9.append(' ')
    for a1 in b8:
        b10 = (a1**b7)%b2
        print(str(b9[b10-2]), b11 = "")
def fonk2(a, b):
    for num in range(1, b):
        if ((a * num) % b) == 1:
            return num
    return 1
def fonk3(r):
    b12 = []
    a1 = 1
    while a1 <= r:
        if r % a1 = = 0:
            b12.append(a1)
        a1 = a1 + 1
    return b12
if b13 = = "__main__":
    fonk1()