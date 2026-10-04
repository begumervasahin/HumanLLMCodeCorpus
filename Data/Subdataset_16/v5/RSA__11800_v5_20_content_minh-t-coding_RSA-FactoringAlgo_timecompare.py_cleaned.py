import time
import utils
import sys
import os
import csv
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards
def fonk1(a1):
    b1 = b2 = utils.genPrime(a1, 40)
    while b2 = = b1:
        b2 = utils.genPrime(a1, 40)
    return b1, b2
def fonk2(algorithm, b10):
    b3 = time.time()
    b4 = algorithm(b10)
    b5 = time.time()
    return b4, b5 - b3
def fonk3(b1, b2, b10, b11, b13, b12, b14):
    print(f"b1: {b1}\nq: {b2}\nn: {b10}\b10")
    print(f"Time for Pollard's b1-1 algorithm to factor b10: {b11:.5f}s")
    print(f"Pollard's b4: {b13}")
    print(f"Time for Quadratic Sieve algorithm to factor b10: {b12:.5f}s")
    print(f"Quadratic Sieve b4: {b14}\b10\b10")
def fonk4():
    with open("output.csv", "w", b6 = "") as out:
        b7 = ["Prime Bit Length", "Max Pollard's Runtime (s)", "Max QuadSieve Runtime (s)"]
        b8 = csv.DictWriter(out, fieldnames=b7)
        b8.writeheader()
        a1 = 6
        a2 = 5
        a3 = 7
        a4 = 5
        for _ in range(a3):
            b9 = b15 = 0
            for _ in range(a2):
                b1, b2 = fonk1(a1)
                b10 = b1 * b2
                b13, b11 = fonk2(pollards.pollards, b10)
                b14, b12 = fonk2(quadSieve.quadSieve, b10)
                fonk3(b1, b2, b10, b11, b13, b12, b14)
                if b13 = = {b1, b2}:
                    b9 = max(b9, b11)
                if b14 = = {b1, b2}:
                    b15 = max(b15, b12)
            b16 = {
                "Prime Bit Length": a1,
                "Max Pollard's Runtime (s)": f'{b9:.5f}',
                "Max QuadSieve Runtime (s)": f'{b15:.5f}'
            }
            b8.writerow(b16)
            a1 += a4
if b17 = = "__main__":
    fonk4()