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
    for i in range(a3):
        b5 = quad_failures = 0
        b6 = b15 = 0
        for sample in range(a2):
            b7 = p = utils.genPrime(a1, 40)
            while b7 = = p:
                b7 = utils.genPrime(a1, 40)
            b8 = p * b7
            print("p: {}\nq: {}\nn: {}\b8".format(p, b7, b8))
            b9 = time.time()
            b10 = pollards.pollards(b8)
            b11 = time.time()
            b12 = b11 - b9
            print("Time for Pollard's p-1 algorithm to factor b8: {}s".format(b12))
            print("Pollards result: {}".format(b10))
            b9 = time.time()
            b13 = quadSieve.quadSieve(b8)
            b11 = time.time()
            b14 = b11 - b9
            print("Time for Quad. Sieve algorithm to factor b8: {}s".format(b14))
            print("Quad. Sieve result: {}\b8\b8".format(b13))
            if b10 != {p, b7}:
                b5 += 1
            else:
                b6 = max(b6, b12)
            if b13 != {p, b7}:
                quad_failures += 1
            else:
                b15 = max(b15, b14)
        b16 = {
            "Prime Bit Length": a1,
            "Max Pollard's Runtime (s)": '{0:.5f}'.format(b6),
            "Max QuadSieve Runtime (s)": '{0:.5f}'.format(b15),
            "Pollard's Failures": b5,
            "QuadSieve Failures": quad_failures
        }
        b4.writerow(b16)
        a1 += a4
print(f"Results written to {b1}")