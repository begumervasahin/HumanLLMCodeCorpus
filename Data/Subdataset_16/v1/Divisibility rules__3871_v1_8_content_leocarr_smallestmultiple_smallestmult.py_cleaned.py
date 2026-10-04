def fonk1(b3):
    b1 = b3
    while True:
        if all(b1 % b2 = = 0 for b2 in range(1, b3 + 1)):
            return b1
        b1 += b3
def fonk2():
    b3 = int(input("What is the max multiple? "))
    b4 = fonk1(b3)
    print(f"The smallest number that is evenly divisible by all of the numbers from 1 to {b3} is {b4}")
if b5 = = "__main__":
    fonk2()