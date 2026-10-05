def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, number):
        if number % b1 = = 0:
            return False
    return True
if b2 = = "__main__":
    b3 = int(input("Please enter an integer you want to check: "))
    b4 = fonk1(b3)
    if b4:
        print(str(b3) + " is a prime number")
    else:
        print(str(b3) + " is not a prime number")