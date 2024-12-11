import random
def fonk1(b5):
    a1 = 10
    a2 = 2
    while a2 < b5:
        if all(a1 % i != 0 for i in range(2, a1)):
            a2 += 1
        a1 += 1
    return a1 - 1
def fonk2(num):
    return all(num % i != 0 for i in range(2, num))
def fonk3(b5):
    a3 = 0
    a1 = 10
    while a3 < b5:
        if fonk2(a1):
            b1 = 2 ** a1 - 1
            if fonk2(b1):
                a3 += 1
        a1 += 1
    return b1
def fonk4(b5):
    b2 = fonk3(b5)
    with open(f'monisen_{b5}.txt', 'w') as file:
        file.write(str(b2))
def fonk5(num, base):
    if num >= base:
        fonk5(num
    print(num % base, b3 = ' ')
if b4 = = "__main__":
    b5 = int(input("Enter the value of b5: "))
    print("6th prime a1:", fonk1(6))
    print("6th Monisen a1:", fonk3(6))
    fonk4(6)
    b6 = int(input("Enter the first a1: "))
    b7 = int(input("Enter the base: "))
    fonk5(b6, b7)