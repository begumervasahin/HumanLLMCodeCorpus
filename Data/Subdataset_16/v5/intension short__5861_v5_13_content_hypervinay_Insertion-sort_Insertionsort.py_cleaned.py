import time
import sys
def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i
        while b2 > 0 and b3[b2 - 1] > b1:
            b3[b2] = b3[b2 - 1]
            b2 -= 1
        b3[b2] = b1
def fonk2(filename):
    with open(filename, 'r') as file:
        return [int(number) for number in file.read().strip().split(',')]
def fonk3(filename, b3):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, b3)))
def fonk4(b7, b8):
    b3 = fonk2(b7)
    b4 = time.time()
    fonk1(b3)
    b5 = time.time() - b4
    print(f"Sorting completed in {b5:.6f} seconds")
    fonk3(b8, b3)
if b6 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <b7> <b8>")
        sys.exit(1)
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    fonk4(b7, b8)