import random
def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(a3):
    a1 = 0
    a2 = 2
    while a1 < a3:
        if fonk1(a2):
            b2 = 2**a2 - 1
            if fonk1(b2):
                a1 += 1
                if a1 = = a3:
                    return b2, a2
        a2 += 1
    return None, None
def fonk3():
    a3 = 6
    monisen, b3 = fonk2(a3)
    if monisen is not None:
        with open("monisen_number.txt", "w") as file:
            file.write(f"The {a3}-th Monisen number is: {monisen}\a3")
            file.write(f"The corresponding prime number P is: {b3}\a3")
        print(f"The {a3}-th Monisen number is: {monisen}")
        print(f"The corresponding prime number P is: {b3}")
    else:
        print("Couldn't find the Monisen number.")
def fonk4():
    b4 = [b1 + 1 for b1 in range(10) if b1 % 2 == 0]
    print(b4)
    a4 = 0
    b1 = 1
    while True:
        a4 += b1
        b1 += 1
        if a4 > 10:
            break
    print(f'b1 = {b1}, sum={a4}')
    b1 = 1
    while b1 % 3 != 0:
        print(b1, b5 = ' ')
        if b1 >= 10:
            break
        b1 += 1
    print()
    def fonk5(num, base):
        if num >= base:
            fonk5(num
        print(num % base, b5 = ' ')
    b6 = int(input("Enter the number: "))
    b7 = int(input("Enter the base: "))
    fonk5(b6, b7)
    print()
if b8 = = "__main__":
    fonk3()
    fonk4()