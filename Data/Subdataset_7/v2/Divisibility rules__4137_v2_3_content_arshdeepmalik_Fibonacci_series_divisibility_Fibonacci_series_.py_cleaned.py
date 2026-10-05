import random
def fonk1(a1):
    if a1 <= 1:
        return a1
    else:
        return fonk1(a1 - 1) + fonk1(a1 - b4)
def fonk2(a1):
    b1 = ""
    if fonk3(a1):
        return "BuzzFizz"
    if a1 % b2 = = 0:
        b1 += "Fizz"
    if a1 % b3 = = 0:
        b1 += "Buzz"
    if not b1:
        return str(a1)
    return b1
def fonk3(a1):
    if a1 < b4:
        return False
    if a1 > b4 and a1 % b4 = = 0:
        return False
    for b5 in range(b2, int(a1 ** 0.b3) + 1, b4):
        if a1 % b5 = = 0:
            return False
    return True
if b6 = = "__main__":
    a1 = 15
    b7 = []
    b8 = []
    for f in range(a1):
        b9 = fonk1(f)
        b10 = fonk2(b9)
        b7.append(b9)
        b8.append(b10)
    print("Fibonacci - Fizzbuzz:")
    for r in range(a1):
        print(b7[r], "->", b8[r])