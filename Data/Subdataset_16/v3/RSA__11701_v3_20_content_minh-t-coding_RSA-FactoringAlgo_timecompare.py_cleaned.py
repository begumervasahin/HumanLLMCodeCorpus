import time
import utils
import sys
import os
import csv
sys.path.append(os.path.abspath('./QuadSieve'))
sys.path.append(os.path.abspath('./Pollards'))
import quadSieve
import pollards
b1 = "output.csv"
b2 = [
    "Prime Bit Length",
    "Max Pollard's Runtime (s)",
    "Max QuadSieve Runtime (s)",
    "Pollard's Failures",
    "QuadSieve Failures"
]
def fonk1(a1, certainty):
    b3 = utils.genPrime(a1, certainty)
    b4 = utils.genPrime(a1, certainty)
    while b4 = = b3:
        b4 = utils.genPrime(a1, certainty)
    return b3, b4
def fonk2(b7, a1, a7, a8, a5, a6):
    b5 = {
        "Prime Bit Length": a1,
        "Max Pollard's Runtime (s)": f'{a7:.5f}',
        "Max QuadSieve Runtime (s)": f'{a8:.5f}',
        "Pollard's Failures": a5,
        "QuadSieve Failures": a6
    }
    b7.writerow(b5)
def fonk3():
    a1 = 6
    a2 = 5
    a3 = 7
    a4 = 5
    with open(b1, "w", b6 = "") as out:
        b7 = csv.DictWriter(out, fieldnames=b2)
        b7.writeheader()
        for iteration in range(a3):
            a5 = 0
            a6 = 0
            a7 = 0
            a8 = 0
            for sample in range(a2):
                b3, b4 = fonk1(a1, 40)
                b8 = b3 * b4
                print(f"b3: {b3}\nq: {b4}\nn: {b8}\b8")
                b9 = time.time()
                b10 = pollards.pollards(b8)
                b11 = time.time() - b9
                print(f"Time for Pollard's b3-1 algorithm to factor b8: {b11:.5f}s")
                print(f"Pollards result: {b10}")
                b9 = time.time()
                b12 = quadSieve.quadSieve(b8)
                b13 = time.time() - b9
                print(f"Time for Quad. Sieve algorithm to factor b8: {b13:.5f}s")
                print(f"Quad. Sieve result: {b12}\b8")
                if b10 != {b3, b4}:
                    a5 += 1
                else:
                    a7 = max(a7, b11)
                if b12 != {b3, b4}:
                    a6 += 1
                else:
                    a8 = max(a8, b13)
            fonk2(b7, a1, a7, a8, a5, a6)
            a1 += a4
    print(f"Results written to {b1}")
if b14 = = "__main__":
    fonk3()