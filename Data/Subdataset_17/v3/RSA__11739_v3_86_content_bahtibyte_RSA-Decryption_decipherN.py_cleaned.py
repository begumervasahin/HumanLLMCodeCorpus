import multiprocessing
import math
import time
import os
def format_number(num):
    return "{:,}".format(num)
def found(core, p, q, n, start_time, end_time):
    print(f"Core {core} successfully found p * q\n")
    print(f"P: {p}\nq: {q}\n\n{format_number(p)} * {format_number(q)} = {format_number(n)}")
    print(f"\nDecrypting p and q took {(end_time - start_time) / 60:.2f} mins")
def analyze(core, n, start_range, end_range):
    print(f"Core {core} starting to analyze {format_number(6 * start_range - 1)} to {format_number(6 * end_range + 1)}")
    process_start_time = time.time()
    p = 6 * start_range + 1
    for _ in range(end_range - start_range + 1):
        p += 4
        if n % p == 0:
            q = n
            found(core, p, q, n, process_start_time, time.time())
            return
        p += 2
        if n % p == 0:
            q = n
            found(core, p, q, n, process_start_time, time.time())
            return
    print(f"Core {core} analyzed {format_number(start_range)} to {format_number(end_range)}! Took {(time.time() - process_start_time) / 60:.2f} mins")
def main():
    start_time = time.time()
    user_p = 776533697
    user_q = 37270792891
    n = user_p * user_q
    max_index = math.ceil(math.sqrt(n) / 6)
    print("===========================================================")
    print(f"Starting Decryption!\nGiven N = {format_number(n)}")
    print(f"\nTotal number of primes under N is {format_number(max_index * 2)}")
    print(f"Each Core calculates {format_number(int(max_index / 4))}\n")
    processes = []
    num_cores = os.cpu_count()
    division = math.ceil(max_index / num_cores)
    for i in range(num_cores):
        start_range = division * i + 1
        end_range = division * (i + 1)
        process = multiprocessing.Process(target=analyze, args=(i, n, start_range, end_range))
        processes.append(process)
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print(f"\nFinished Decryption. Process Finished! Took {(end_time - start_time):.2f} seconds")
    print("===========================================================")
if __name__ == "__main__":
    main()