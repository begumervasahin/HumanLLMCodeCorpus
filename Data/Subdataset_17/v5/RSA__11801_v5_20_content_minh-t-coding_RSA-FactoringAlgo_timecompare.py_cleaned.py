import time
import utils
import sys
import os
import csv
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards
def generate_prime_pair(bitlength):
    p = q = utils.genPrime(bitlength, 40)
    while q == p:
        q = utils.genPrime(bitlength, 40)
    return p, q
def measure_runtime(algorithm, n):
    start = time.time()
    result = algorithm(n)
    end = time.time()
    return result, end - start
def log_results(p, q, n, ptime, p_res, qtime, q_res):
    print(f"p: {p}\nq: {q}\nn: {n}\n")
    print(f"Time for Pollard's p-1 algorithm to factor n: {ptime:.5f}s")
    print(f"Pollard's result: {p_res}")
    print(f"Time for Quadratic Sieve algorithm to factor n: {qtime:.5f}s")
    print(f"Quadratic Sieve result: {q_res}\n\n")
def main():
    with open("output.csv", "w", newline="") as out:
        fieldNames = ["Prime Bit Length", "Max Pollard's Runtime (s)", "Max QuadSieve Runtime (s)"]
        outWriter = csv.DictWriter(out, fieldnames=fieldNames)
        outWriter.writeheader()
        bitlength = 6
        sampleSize = 5
        niterations = 7
        bitincrement = 5
        for _ in range(niterations):
            polMaxTime = quadMaxTime = 0
            for _ in range(sampleSize):
                p, q = generate_prime_pair(bitlength)
                n = p * q
                p_res, ptime = measure_runtime(pollards.pollards, n)
                q_res, qtime = measure_runtime(quadSieve.quadSieve, n)
                log_results(p, q, n, ptime, p_res, qtime, q_res)
                if p_res == {p, q}:
                    polMaxTime = max(polMaxTime, ptime)
                if q_res == {p, q}:
                    quadMaxTime = max(quadMaxTime, qtime)
            writeData = {
                "Prime Bit Length": bitlength,
                "Max Pollard's Runtime (s)": f'{polMaxTime:.5f}',
                "Max QuadSieve Runtime (s)": f'{quadMaxTime:.5f}'
            }
            outWriter.writerow(writeData)
            bitlength += bitincrement
if __name__ == "__main__":
    main()