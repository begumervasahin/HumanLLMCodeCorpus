def fonk1(num):
    b1 = b3 = 0
    while num:
        if num & 1:
            b1 += 1
        num >>= 1
        if num & 1:
            b3 += 1
        num >>= 1
    return b1, b3
def fonk2(b2):
    if b2 = = 0:
        return True
    elif b2 = = 1:
        return False
    b1, b3 = fonk1(abs(b2))
    b4 = abs(b1 - b3)
    return fonk2(b4)
if b5 = = "__main__":
    try:
        b2 = int(input("Enter an integer: "))
        if fonk2(abs(b2)):
            print("%d is divisible by 3." % b2)
        else:
            print("%d is not divisible by 3." % b2)
    except ValueError:
        print("Invalid input. Please enter an integer.")