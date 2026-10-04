def fonk1(b2):
    if b2 <= 1:
        return False
    for b1 in range(2, int(b2 ** 0.5) + 1):
        if b2 % b1 = = 0:
            return False
    return True
def fonk2():
    try:
        b2 = int(input("Please enter an integer you want to check: "))
        if fonk1(b2):
            print(f"{b2} is a prime b2")
        else:
            print(f"{b2} is not a prime b2")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if b3 = = "__main__":
    fonk2()