def fonk1(number):
    try:
        int(number)
        return True
    except ValueError:
        print("User Input Not an Integer")
        return False
def fonk2(number):
    if number < 2:
        print(str(number) + ' is not a prime number')
        return False
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            print(str(number) + ' is not a prime number')
            return False
    print(str(number) + ' is a prime number')
    return True
b2 = ""
while b2 != "stop":
    b2 = input("Enter a Number: ")
    if fonk1(b2):
        fonk2(int(b2))