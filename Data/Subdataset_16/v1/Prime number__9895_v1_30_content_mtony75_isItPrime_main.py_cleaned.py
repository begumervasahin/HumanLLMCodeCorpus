def fonk1(number):
    try:
        int(number)
        return True
    except ValueError:
        print("User Input is not an integer")
        return False
def fonk2(number):
    if number < 2:
        print(f"{number} is not a prime number")
        return False
    for b1 in range(2, number):
        if number % b1 = = 0:
            print(f"{number} is not a prime number")
            return False
    print(f"{number} is a prime number")
    return True
while True:
    b2 = input("Enter a number (or type 'stop' to end): ")
    if b2.lower() == 'stop':
        break
    if fonk1(b2):
        fonk2(int(b2))