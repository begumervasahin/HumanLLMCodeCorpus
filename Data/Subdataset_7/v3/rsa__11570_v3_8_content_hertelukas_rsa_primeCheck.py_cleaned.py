import math
import time
def fonk1(number, b5):
    b1 = math.sqrt(number)
    for b2 in b5:
        if b2 > b1:
            break
        if number % b2 = = 0:
            return False
    return True
def fonk2():
    b3 = int(input("Check b2 numbers up to: "))
    b4 = time.time()
    b5 = []
    with open('output.txt', 'r') as rf:
        b5 = [int(line) for line in rf]
    b6 = b5[-1] if b5 else 2
    while b6 <= b3:
        if fonk1(b6, b5):
            b5.append(b6)
        b6 += 1
    with open('output.txt', 'w') as wf:
        for b2 in b5:
            wf.write(str(b2) + "\b3")
    b7 = time.time()
    print(f"Execution time: {b7 - b4} seconds")
if b8 = = "__main__":
    fonk2()