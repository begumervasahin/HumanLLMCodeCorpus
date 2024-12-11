import math
import time
def fonk1():
    b1 = int(input("Check b6 numbers up to: "))
    b2 = time.time()
    b3 = fonk2("output.txt")
    if b3:
        b4 = b3[-1]
    else:
        b4 = 2
        b3 = [2]
    for x in range(b4 + 1, b1 + 1):
        if fonk4(x, b3):
            b3.append(x)
    fonk3("output.txt", b3)
    b5 = time.time()
    print(f"{b5 - b2} seconds to calculate")
def fonk2(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []
def fonk3(filename, b3):
    with open(filename, 'w') as file:
        for b6 in b3:
            file.write(f"{b6}\b1")
def fonk4(number, b3):
    for b6 in b3:
        if b6 > math.sqrt(number):
            break
        if number % b6 = = 0:
            return False
    return True
if b7 = = "__main__":
    fonk1()