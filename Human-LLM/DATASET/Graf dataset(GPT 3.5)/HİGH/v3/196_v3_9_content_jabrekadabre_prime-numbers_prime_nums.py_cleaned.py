def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
if b2 = = '__main__':
    b3 = int(input("Enter the value of a: "))
    if fonk1(b3):
        print("The given number is prime.")
    else:
        print("The given number is not prime.")