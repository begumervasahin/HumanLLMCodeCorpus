def fonk1(num):
    if num < 2:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
if b2 = = "__main__":
    b3 = int(input("Please enter an integer you want to check: "))
    if fonk1(b3):
        print(f"{b3} is a prime number")
    else:
        print(f"{b3} is not a prime number")