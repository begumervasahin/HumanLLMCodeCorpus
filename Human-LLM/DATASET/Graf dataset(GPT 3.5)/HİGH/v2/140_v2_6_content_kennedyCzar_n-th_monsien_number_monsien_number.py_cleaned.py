import random
def fonk1(b6):
    a1 = 2
    a2 = 0
    while a2 < b6:
        if fonk2(a1):
            a2 += 1
        a1 += 1
    return a1 - 1
def fonk2(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk3(b6):
    a3 = 0
    a1 = 2
    while True:
        if fonk2(a1):
            b2 = 2 ** a1 - 1
            if fonk2(b2):
                a3 += 1
                if a3 = = b6:
                    return b2
        a1 += 1
def fonk4(b6):
    b3 = fonk3(b6)
    with open(f'monisen_{b6}.txt', 'w') as file:
        file.write(str(b3))
def fonk5(num, base):
    if num >= base:
        fonk5(num
    print(num % base, b4 = ' ')
if b5 = = "__main__":
    b6 = int(input("Enter the value of b6: "))
    print("6th prime a1:", fonk1(6))
    print("6th Monisen a1:", fonk3(6))
    fonk4(6)
    b7 = int(input("Enter the first a1: "))
    b8 = int(input("Enter the base: "))
    fonk5(b7, b8)