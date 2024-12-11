def fonk1(number):
    if number < 2:
        return False
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2():
    b2 = int(input("Enter the value of 'b2': "))
    if fonk1(b2):
        print("The given number is prime.")
    else:
        print("The given number is not prime.")
if b3 = = "__main__":
    fonk2()