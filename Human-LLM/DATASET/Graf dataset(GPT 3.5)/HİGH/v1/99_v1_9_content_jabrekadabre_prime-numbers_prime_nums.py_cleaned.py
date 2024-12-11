b1 = int(input("Enter the value of b1: "))
def fonk1(num):
    if num < 2:
        return False
    for b2 in range(2, int(num ** 0.5) + 1):
        if num % b2 = = 0:
            return False
    return True
if fonk1(b1):
    print("The given number is b1 prime.")
else:
    print("The given number is not b1 prime.")