def fonk1(b1):
    while b1 not in {'Y', 'y', 'N', 'n'}:
        b1 = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
a1 = 0
a2 = 0
b2 = 'y'
a3 = 1
a4 = 0
a5 = 0
b3 = False
while True:
    try:
        a1 = int(input("Please enter the first positive integer: "))
        if a1 < 0:
            raise ValueError
        a2 = int(input("Please enter the second positive integer: "))
        if a2 < 0:
            raise ValueError
        break
    except ValueError:
        print("Value error. Remember that this program will only take positive INTEGERS. Starting over.\n")
print("Your first number is", a1, "and your second number is", a2)
b2 = input("Are these correct? ")
fonk1(b2)
if not b3:
    a6 = 1
    while a3 - 10 * (a3 / 10) != 9:
        a3 = a2 * a6
        a6 += 1
    a3 = (a3 / 10) + 1
print("Your X Factor is", a3)
a4 = a1 - 10 * (a1 / 10)
a4 *= a3
a5 = int(a1 / 10)
a5 += a4
print("Is", a5, "divisible by", a2, "?")