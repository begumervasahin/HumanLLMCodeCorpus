import time
import utils
import sys
import os
import csv
sys.path.append(os.path.abspath('./QuadSieve'))
sys.path.append(os.path.abspath('./Pollards'))
import quadSieve
import pollards
output_file = "output.csv"
field_names = ["Prime Bit Length", "Max Pollard's Runtime (s)", "Max QuadSieve Runtime (s)",
               "Pollard's Failures", "QuadSieve Failures"]
with open(output_file, "w", newline="") as out:
    out_writer = csv.DictWriter(out, fieldnames=field_names)
    out_writer.writeheader()
    bitlength = 6
    sample_size = 5
    niterations = 7
    bitincrement = 5
    for iteration in range(niterations):
        pol_failures = 0
        quad_failures = 0
        pol_max_time = 0
        quad_max_time = 0
        for sample in range(sample_size):
            q = p = utils.genPrime(bitlength, 40)
            while q == p:
                q = utils.genPrime(bitlength, 40)
            n = p * q
            print(f"p: {p}\nq: {q}\nn: {n}\n")
            start_time = time.time()
            p_res = pollards.pollards(n)
            end_time = time.time()
            p_time = end_time - start_time
            print(f"Time for Pollard's p-1 algorithm to factor n: {p_time:.5f}s")
            print(f"Pollards result: {p_res}")
            start_time = time.time()
            q_res = quadSieve.quadSieve(n)
            end_time = time.time()
            q_time = end_time - start_time
            print(f"Time for Quad. Sieve algorithm to factor n: {q_time:.5f}s")
            print(f"Quad. Sieve result: {q_res}\n")
            if p_res != {p, q}:
                pol_failures += 1
            else:
                pol_max_time = max(pol_max_time, p_time)
            if q_res != {p, q}:
                quad_failures += 1
            else:
                quad_max_time = max(quad_max_time, q_time)
        write_data = {
            "Prime Bit Length": bitlength,
            "Max Pollard's Runtime (s)": f'{pol_max_time:.5f}',
            "Max QuadSieve Runtime (s)": f'{quad_max_time:.5f}',
            "Pollard's Failures": pol_failures,
            "QuadSieve Failures": quad_failures
        }
        out_writer.writerow(write_data)
        bitlength += bitincrement
print(f"Results written to {output_file}")