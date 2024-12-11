import math
def fonk1(x):
    b1 = [i for i in range(1, math.ceil(x / 2) + 1) if x % i == 0]
    return sum(b1)
def fonk2(a1):
    b2 = []
    for num in range(12, a1):
        if fonk1(num) > num:
            b2.append(num)
    return b2
def fonk3(b2):
    b3 = set()
    for i in range(len(b2)):
        for j in range(len(b2)):
            if b2[i] + b2[j] < 28123:
                b3.add(b2[i] + b2[j])
    return b3
def fonk4(a1, b3):
    b4 = sum(num for num in range(a1) if num not in b3)
    return b4
if b5 = = "__main__":
    a1 = 28123
    print("Finding abundant numbers...")
    b2 = fonk2(a1)
    print("Finding sum of two abundant numbers...")
    b3 = fonk3(b2)
    print("Finding sum of all positive integers that cannot be written as the sum of two abundant numbers...")
    b4 = fonk4(a1, b3)
    print("The sum of all positive integers that cannot be written as the sum of two abundant numbers is:", b4)