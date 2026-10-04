import random
def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(b4):
    a1 = 0
    a2 = 2
    while a1 < b4:
        if fonk1(a2):
            b2 = 2 ** a2 - 1
            if fonk1(b2):
                a1 += 1
                if a1 = = b4:
                    return b2
        a2 += 1
def fonk3(num, base):
    if num >= base:
        fonk3(num
    print(num % base, b3 = ' ')
def fonk4():
    b4 = int(input("Enter the nth Monisen number: "))
    b5 = fonk2(b4)
    print(f"The {b4}-th Monisen number is: {b5}")
    with open("monisen_number.txt", "w") as file:
        file.write(str(b5))
    b6 = int(input("Enter a number: "))
    b7 = int(input("Enter the base: "))
    fonk3(b6, b7)
    print()
if b8 = = "__main__":
    fonk4()