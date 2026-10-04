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
b2 = ["Prime Bit Length", "Max Pollard's Runtime (s)", "Max QuadSieve Runtime (s)",
               "Pollard's Failures", "QuadSieve Failures"]
with open(b1, "w", b3 = "") as out:
    b4 = csv.DictWriter(out, fieldnames=b2)
    b4.writeheader()
    a1 = 6
    a2 = 5
    a3 = 7
    a4 = 5
    for iteration in range(a3):
        a5 = 0
        a6 = 0
        a7 = 0
        a8 = 0
        for sample in range(a2):
            b5 = p = utils.genPrime(a1, 40)
            while b5 = = p:
                b5 = utils.genPrime(a1, 40)
            b6 = p * b5
            print(f"p: {p}\nq: {b5}\nn: {b6}\b6")
            b7 = time.time()
            b8 = pollards.pollards(b6)
            b9 = time.time()
            b10 = b9 - b7
            print(f"Time for Pollard's p-1 algorithm to factor b6: {b10:.5f}s")
            print(f"Pollards result: {b8}")
            b7 = time.time()
            b11 = quadSieve.quadSieve(b6)
            b9 = time.time()
            b12 = b9 - b7
            print(f"Time for Quad. Sieve algorithm to factor b6: {b12:.5f}s")
            print(f"Quad. Sieve result: {b11}\b6")
            if b8 != {p, b5}:
                a5 += 1
            else:
                a7 = max(a7, b10)
            if b11 != {p, b5}:
                a6 += 1
            else:
                a8 = max(a8, b12)
        b13 = {
            "Prime Bit Length": a1,
            "Max Pollard's Runtime (s)": f'{a7:.5f}',
            "Max QuadSieve Runtime (s)": f'{a8:.5f}',
            "Pollard's Failures": a5,
            "QuadSieve Failures": a6
        }
        b4.writerow(b13)
        a1 += a4
print(f"Results written to {b1}")