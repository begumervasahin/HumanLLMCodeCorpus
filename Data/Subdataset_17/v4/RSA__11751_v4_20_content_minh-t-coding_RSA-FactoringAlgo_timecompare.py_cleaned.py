import time
import utils
import sys
import os
import csv
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards
with open("output.csv", "w", newline="") as out:
    fieldNames = ["Prime Bit Length", "Max Pollard's Runtime (s)", "Max QuadSieve Runtime (s)"]
    outWriter = csv.DictWriter(out, fieldnames=fieldNames)
    outWriter.writeheader()
    bitlength = 6
    sampleSize = 5
    niterations = 7
    bitincrement = 5
    for i in range(niterations):
        polFailures = quadFailures = 0
        polMaxTime = quadMaxTime = 0
        for sample in range(sampleSize):
            p = q = utils.genPrime(bitlength, 40)
            while q == p:
                q = utils.genPrime(bitlength, 40)
            n = p * q
            print(f"p: {p}\nq: {q}\nn: {n}\n")
            start = time.time()
            p_res = pollards.pollards(n)
            end = time.time()
            ptime = end - start
            print(f"Time for Pollard's p-1 algorithm to factor n: {ptime}s")
            print(f"Pollards result: {p_res}")
            start = time.time()
            q_res = quadSieve.quadSieve(n)
            end = time.time()
            qtime = end - start
            print(f"Time for Quad. Sieve algorithm to factor n: {qtime}s")
            print(f"Quad. Sieve result: {q_res}\n\n")
            if p_res != {p, q}:
                polFailures += 1
            else:
                polMaxTime = max(polMaxTime, ptime)
            if q_res != {p, q}:
                quadFailures += 1
            else:
                quadMaxTime = max(quadMaxTime, qtime)
        writeData = {
            "Prime Bit Length": bitlength,
            "Max Pollard's Runtime (s)": f'{polMaxTime:.5f}',
            "Max QuadSieve Runtime (s)": f'{quadMaxTime:.5f}'
        }
        outWriter.writerow(writeData)
        bitlength += bitincrement