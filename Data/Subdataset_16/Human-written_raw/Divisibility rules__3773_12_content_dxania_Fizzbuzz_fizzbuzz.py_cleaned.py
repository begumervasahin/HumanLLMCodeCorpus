def fonk1():
    b1 = [n for n in input("Enter the first list (separate elements with commas): ").split(",")]
    print(b1)
    print ("List1 is " + str(len(b1)) + " characters long")
    b2 = [n for n in input("Enter the second list (separate elements with commas): ").split(",")]
    print(b2)
    print ("List2 is " + str(len(b2)) + " characters long")
    print(fonk2(b1, b2))
def fonk2(a, b):
    b3 = len(a) + len(b)
    if b3 % b4 = = 0:
        return 'Fizz'
    elif b3 % b5 = = 0:
        return 'Buzz'
    elif b3 % b5 = = 0 and b3 % b4 == 0:
        return 'FizzBuzz'
    else:
        return b3
fonk1()