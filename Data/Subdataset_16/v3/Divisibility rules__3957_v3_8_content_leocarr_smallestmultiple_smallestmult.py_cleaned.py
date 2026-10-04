def fonk1(b4):
    b1 = b4
    while True:
        if all(b1 % b2 = = 0 for b2 in range(1, b4 + 1)):
            return b1
        b1 += b4
def fonk2(prompt):
    while True:
        try:
            b3 = int(input(prompt))
            if b3 < 1:
                print("Please enter a positive integer greater than zero.")
            else:
                return b3
        except ValueError:
            print("Please enter a valid integer.")
def fonk3():
    print("Welcome to the Smallest Multiple Finder!")
    b4 = fonk2("What is the max multiple? ")
    b5 = fonk1(b4)
    print(f"The smallest number that is evenly divisible by all of the numbers from 1 to {b4} is {b5}")
if b6 = = "__main__":
    fonk3()