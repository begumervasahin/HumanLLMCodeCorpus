def isItValid(number):
    try:
        int(number)
        return True
    except ValueError:
        print("User Input Not An Integer")
        return False
def isAPrime(number):
    for loopNumber in range(2, number):
        if number % loopNumber == 0:
            print(str(number) + ' is not a prime number')
            return False
    print(str(number) + ' is a prime number')
    return True
usrInput = ""
while usrInput != "stop":
    usrInput = input("Enter a Number: ")
    if isItValid(usrInput):
        isAPrime(int(usrInput))