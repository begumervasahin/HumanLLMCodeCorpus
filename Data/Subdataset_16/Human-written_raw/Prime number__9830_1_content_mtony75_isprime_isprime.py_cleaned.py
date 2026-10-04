'''
Function used to accept input from user
'''
def fonk1():
    b1 = input("Please enter a b5: ")
    b2 = True
    while b2 = = True:
        try:
            b3 = int(b1)
            b2 = False
        except ValueError:
            print(f"The value entered is not an integer")
            b1 = input("Please enter a new value: ")
    return b3
'''
Function used to check if b5 is a prime
'''
def fonk2(b5):
    b4 = False
    if b5 = = 1:
        b4 = False
    elif b5 = = 2:
        b4 = True
    else:
        for b6 in range(2, b5
            if b5 % b6 = = 0:
                b4 = False
                break
            else:
                b4 = True
    return b4
def fonk3():
    print("Give me a range of numbers and find out which numbers in the")
    print("range are prime numbers?")
    b7 = fonk1()
    b8 = fonk1()
    b9 = []
    if b7 < b8:
        b9 = fonk4(b7, b8)
    else:
        b9 = fonk4(b8, b7)
    return b9
def fonk4(num1, num2):
    b10 = []
    for b6 in range(num1, num2+1):
        if fonk2(b6):
            b10.append(b6)
    return b10
def fonk5(b5):
    b11 = b5
    b10 = []
    b12 = b11
    while (len(b10) < 100):
        b12 += 1
        if fonk2(b12):
            b10.append(b12)
    return b10
'''
b11 = fonk1()
print(b11)
if fonk2(b11):
    print(f"{b11} is a Prime")
else:
    print(f"{b11} is not a Prime")
print()
print()
b13 = fonk3()
print(f"The list of primes are {b13}")
print()
print()
b14 = fonk5()
print(f"The list of next 100 primes are {b14}")
'''