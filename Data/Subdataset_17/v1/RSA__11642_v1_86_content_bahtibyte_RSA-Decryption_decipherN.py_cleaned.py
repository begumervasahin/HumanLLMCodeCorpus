import multiprocessing
import math
import time
import os
def format_number(num):
    return "{:,}".format(num)
def found(c, p, q, n, s, e):
    print("Core ", c, " successfully found p * q\n")
    print("P: ", p, "\nq: ", q, "\n\n" + format_number(p), " * ", format_number(q), " = ", format_number(n))
    print("\nDecrypting p and q took ", "{0:.2f}".format((e - s) / 60), " mins")
def analyze(c, n, s, e):
    print("Core ", c, " starting to analyze ", format_number(6 * s - 1), " to ", format_number(6 * e + 1))
    p_start_time = time.time()
    p = 6 * s + 1
    for i in range(e - s + 1):
        p += 4
        if n % p == 0:
            q = int(n / p)
            found(c, p, q, n, p_start_time, time.time())
            return
        p += 2
        if n % p == 0:
            q = int(n / p)
            found(c, p, q, n, p_start_time, time.time())
            return
    print("Core ", c, " analyzed ", format_number(s), " to ", format_number(e), "! Took ", "{0:.2f}".format((time.time() - p_start_time) / 60), " mins")
def main():
    start_time = time.time()
    user_p = 776533697
    user_q = 37270792891
    n = user_p * user_q
    max_i = math.ceil(math.sqrt(n) / 6)
    print("===========================================================")
    print("Starting Decryption!\nGiven N = ", "{:,}".format(n))
    print("\nTotal number of primes under N is ", format_number(max_i * 2))
    print("Each Core calculates ", format_number(int(max_i / 4)), "\n")
    processes = []
    div = math.ceil(max_i / os.cpu_count())
    for i in range(os.cpu_count()):
        s = div * i + 1
        e = div * (i + 1)
        processes.append(multiprocessing.Process(target=analyze, args=(i, n, s, e)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print("\nFinished Decryption. Process Finished! Took ", "{0:.2f}".format(end_time - start_time), ' seconds')
    print("===========================================================")
if __name__ == "__main__":
    main