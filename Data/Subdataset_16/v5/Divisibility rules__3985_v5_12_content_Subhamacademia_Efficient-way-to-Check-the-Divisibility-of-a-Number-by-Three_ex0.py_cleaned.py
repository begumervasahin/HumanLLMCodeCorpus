def fonk1(b1):
    a1 = 0
    a2 = 0
    if b1 = = 0:
        return True
    if b1 = = 1:
        return False
    while b1:
        if b1 & 1:
            a1 += 1
        b1 >>= 1
        if b1 & 1:
            a2 += 1
        b1 >>= 1
    return fonk1(abs(a1 - a2))
def fonk2():
    try:
        b1 = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if fonk1(abs(b1)):
        print(f"{b1} is divisible by 3.")
    else:
        print(f"{b1} is not divisible by 3.")
if b2 = = "__main__":
    fonk2()