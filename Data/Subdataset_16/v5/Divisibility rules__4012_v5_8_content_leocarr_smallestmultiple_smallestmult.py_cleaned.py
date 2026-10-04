def fonk1(b3):
    b1 = b3
    while True:
        if all(b1 % b2 = = 0 for b2 in range(1, b3 + 1)):
            return b1
        b1 += b3
def fonk2():
    while True:
        try:
            b3 = int(input("What is the max multiple? "))
            if b3 < 1:
                print("Please enter a positive integer greater than zero.")
            else:
                return b3
        except ValueError:
            print("Please enter a valid integer.")
def fonk3():
    print("Welcome to the Smallest Multiple Finder!")
    b3 = fonk2()
    b4 = fonk1(b3)
    print(f"The smallest number that is evenly divisible by all of the numbers from 1 to {b3} is {b4}")
if b5 = = "__main__":
    fonk3()