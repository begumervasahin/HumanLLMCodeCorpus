import multiprocessing
import math
import time
import os
def fonk1(num):
    return "{:,}".format(num)
def fonk2(core, b2, b3, b5, b4, b13):
    print(f"Core {core} successfully found b2 * b3\b5")
    print(f"P: {b2}\nq: {b3}\b5\b5{fonk1(b2)} * {fonk1(b3)} = {fonk1(b5)}")
    print(f"\nDecrypting b2 and b3 took {((b13 - b4) / 60):.2f} mins")
def fonk3(core, b5, b10, b11):
    print(f"Core {core} starting to analyze {fonk1(6 * b10 - 1)} to {fonk1(6 * b11 + 1)}")
    b1 = time.time()
    b2 = 6 * b10 + 1
    for _ in range(b11 - b10 + 1):
        b2 += 4
        if b5 % b2 = = 0:
            b3 = b5
            fonk2(core, b2, b3, b5, b1, time.time())
            return
        b2 += 2
        if b5 % b2 = = 0:
            b3 = b5
            fonk2(core, b2, b3, b5, b1, time.time())
            return
    print(f"Core {core} analyzed {fonk1(b10)} to {fonk1(b11)}! Took {(time.time() - b1) / 60:.2f} mins")
def fonk4():
    b4 = time.time()
    a1 = 776533697
    a2 = 37270792891
    b5 = a1 * a2
    b6 = math.ceil(math.sqrt(b5) / 6)
    print("===========================================================")
    print(f"Starting Decryption!\nGiven b7 = {fonk1(b5)}")
    print(f"\nTotal number of primes under b7 is {fonk1(b6 * 2)}")
    print(f"Each Core calculates {fonk1(int(b6 / 4))}\b5")
    b8 = []
    b9 = math.ceil(b6 / os.cpu_count())
    for i in range(os.cpu_count()):
        b10 = b9 * i + 1
        b11 = b9 * (i + 1)
        b12 = multiprocessing.Process(target=analyze, args=(i, b5, b10, b11))
        b8.append(b12)
    for b12 in b8:
        b12.start()
    for b12 in b8:
        b12.join()
    b13 = time.time()
    print(f"\nFinished Decryption. Process Finished! Took {(b13 - b4):.2f} seconds")
    print("===========================================================")
if b14 = = "__main__":
    fonk4()