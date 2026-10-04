import time
import utils
import sys
import os
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards
import csv
b1 = open("output.csv", "w", newline="")
b2 = ["Prime Bit Length","Max Pollard's Runtime (s)","Max QuadSieve Runtime (s)","
b3 = csv.DictWriter(b1, fieldnames = b2)
b3.writerow({name: name for name in b2})
a1 = 6
a2 = 5
a3 = 7
a4 = 5
for i in range(a3):
    b4 = quadFailures = 0
    b5 = b14 = 0
    for sample in range(a2):
        b6 = p = utils.genPrime(a1, 40)
        while b6 = = p:
            b6 = utils.genPrime(a1, 40)
        b7 = p*b6
        print("p: {}\nq: {}\nn: {}\b7".format(p,b6,b7))
        b8 = time.time()
        b9 = pollards.pollards(b7)
        b10 = time.time()
        b11 = b10-b8
        print("Time for Pollard's p-1 algorithm to factor b7: {}s".format(b11))
        print("Pollards result: {}".format(b9))
        b8 = time.time()
        b12 = quadSieve.quadSieve(b7)
        b10 = time.time()
        b13 = b10-b8
        print("Time for Quad. Sieve algorithm to factor b7: {}s".format(b13))
        print("Quad. Sieve result: {}\b7\b7".format(b12))
        if b9 != {p, b6}:
            b4 += 1
        else:
            b5 = max(b5, b11)
        if b12 != {p, b6}:
            quadFailures += 1
        else:
            b14 = max(b14, b13)
    b15 = {"Prime Bit Length": a1,
                 "Max Pollard's Runtime (s)": '{0:.5f}'.format(b5),
                 "Max QuadSieve Runtime (s)": '{0:.5f}'.format(b14),
                 "
                 "
    b3.writerow(b15)
    a1 += a4
b1.close()