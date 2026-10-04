import multiprocessing
import math
import time
import os
def fonk1(num):
    return "{:,}".format(num)
def fonk2(core, b3, b4, b6, b5, b15):
    b1 = (b15 - b5) / 60
    print(f"Core {core} successfully found b3 * b4\b6")
    print(f"P: {b3}\nq: {b4}\b6\b6{fonk1(b3)} * {fonk1(b4)} = {fonk1(b6)}")
    print(f"\nDecrypting b3 and b4 took {b1:.2f} mins")
def fonk3(core, b6, b12, b13):
    b2 = time.time()
    print(f"Core {core} starting to analyze {fonk1(6 * b12 - 1)} to {fonk1(6 * b13 + 1)}")
    b3 = 6 * b12 + 1
    for _ in range(b13 - b12 + 1):
        b3 += 4
        if b6 % b3 = = 0:
            b4 = b6
            fonk2(core, b3, b4, b6, b2, time.time())
            return
        b3 += 2
        if b6 % b3 = = 0:
            b4 = b6
            fonk2(core, b3, b4, b6, b2, time.time())
            return
    b1 = (time.time() - b2) / 60
    print(f"Core {core} analyzed {fonk1(b12)} to {fonk1(b13)}! Took {b1:.2f} mins")
def fonk4():
    b5 = time.time()
    a1 = 776533697
    a2 = 37270792891
    b6 = a1 * a2
    b7 = math.ceil(math.sqrt(b6) / 6)
    b8 = os.cpu_count()
    print("===========================================================")
    print(f"Starting Decryption!\nGiven b9 = {fonk1(b6)}")
    print(f"\nTotal number of primes under b9 is {fonk1(b7 * 2)}")
    print(f"Each Core calculates {fonk1(b7
    b10 = []
    b11 = math.ceil(b7 / b8)
    for i in range(b8):
        b12 = b11 * i + 1
        b13 = b11 * (i + 1)
        b14 = multiprocessing.Process(target=analyze, args=(i, b6, b12, b13))
        b10.append(b14)
    for b14 in b10:
        b14.b12()
    for b14 in b10:
        b14.join()
    b15 = time.time()
    b16 = (b15 - b5) / 60
    print(f"\nFinished Decryption. Process Finished! Took {b16:.2f} minutes")
    print("===========================================================")
if b17 = = "__main__":
    fonk4()