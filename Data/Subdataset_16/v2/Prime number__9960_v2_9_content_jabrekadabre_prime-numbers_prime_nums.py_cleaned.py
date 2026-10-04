def fonk1(n):
    if n <= 1:
        return False
    for b1 in range(2, int(n ** 0.5) + 1):
        if n % b1 = = 0:
            return False
    return True
if b2 = = '__main__':
    b3 = int(input("Enter the value of b3: "))
    if fonk1(b3):
        print("The given number is b3 prime")
    else:
        print("The given number is not b3 prime")