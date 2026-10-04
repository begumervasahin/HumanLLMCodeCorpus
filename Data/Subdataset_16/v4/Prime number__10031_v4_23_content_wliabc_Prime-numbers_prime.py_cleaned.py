def fonk1(number):
    if number <= 1:
        return False
    for b1 in range(2, int(number ** 0.5) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2():
    b2 = int(input("Please enter an integer you want to check: "))
    if fonk1(b2):
        print(f"{b2} is a prime number")
    else:
        print(f"{b2} is not a prime number")
if b3 = = "__main__":
    fonk2()