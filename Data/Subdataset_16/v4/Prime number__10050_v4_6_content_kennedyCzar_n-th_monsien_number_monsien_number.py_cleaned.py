import random
def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(b5):
    a1 = 0
    a2 = 2
    while a1 < b5:
        if fonk1(a2):
            b2 = 2**a2 - 1
            if fonk1(b2):
                a1 += 1
                if a1 = = b5:
                    return b2
        a2 += 1
def fonk3(num, base):
    if num >= base:
        fonk3(num
    print(num % base, b3 = ' ')
if b4 = = "__main__":
    b5 = int(input("Enter the nth Monisen number: "))
    b6 = fonk2(b5)
    print(f"The {b5}-th Monisen number is: {b6}")
    with open("monisen_number.txt", "w") as file:
        file.write(str(b6))
    b7 = int(input("Enter a number: "))
    b8 = int(input("Enter the base: "))
    fonk3(b7, b8)
    print()
