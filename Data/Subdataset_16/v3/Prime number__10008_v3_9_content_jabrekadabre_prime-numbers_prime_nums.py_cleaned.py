def fonk1(n):
    if n <= 1:
        return False
    for b1 in range(2, int(n ** 0.5) + 1):
        if n % b1 = = 0:
            return False
    return True
def fonk2():
    b2 = int(input("Enter the value of b2: "))
    if fonk1(b2):
        print("The given number is b2 prime")
    else:
        print("The given number is not b2 prime")
if b3 = = '__main__':
    fonk2()