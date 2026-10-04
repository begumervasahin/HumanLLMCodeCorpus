b1 = int(input("Enter the value of b1: "))
b2 = True
def fonk1(b1):
    global b2
    if b1 <= 1:
        b2 = False
    for b3 in range(2, int(b1 ** 0.5) + 1):
        if b1 % b3 = = 0:
            b2 = False
            break
fonk1(b1)
if b2:
    print("The given number is b1 prime")
else:
    print("The given number is not b1 prime")