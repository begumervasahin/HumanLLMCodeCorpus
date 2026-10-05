import math
import time
def fonk1():
    b1 = fonk2()
    b2 = time.time()
    b3 = fonk3("output.txt")
    b4 = fonk4(b3)
    fonk5(b4, b1, b3)
    fonk7("output.txt", b3)
    b5 = time.time()
    fonk8(b2, b5)
def fonk2():
    return int(input("Please enter the upper limit for b6 number generation: "))
def fonk3(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []
def fonk4(b3):
    return b3[-1] if b3 else 2
def fonk5(b4, b1, b3):
    for num in range(b4 + 1, b1 + 1):
        if fonk6(num, b3):
            b3.append(num)
def fonk6(number, b3):
    for b6 in b3:
        if b6 > math.sqrt(number):
            break
        if number % b6 = = 0:
            return False
    return True
def fonk7(filename, b3):
    with open(filename, 'w') as file:
        for b6 in b3:
            file.write(f"{b6}\n")
def fonk8(b2, b5):
    b7 = b5 - b2
    print(f"Prime number generation completed in {b7:.2f} seconds.")
if b8 = = "__main__":
    fonk1()