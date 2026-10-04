def fonk1(b2):
    if b2 <= 1:
        return False
    for b1 in range(2, int(b2 ** 0.5) + 1):
        if b2 % b1 = = 0:
            return False
    return True
def fonk2():
    try:
        b2 = int(input("Enter a b2 to check if it is prime: "))
        if fonk1(b2):
            print("The given b2 is a prime")
        else:
            print("The given b2 is not a prime")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if b3 = = '__main__':
    fonk2()