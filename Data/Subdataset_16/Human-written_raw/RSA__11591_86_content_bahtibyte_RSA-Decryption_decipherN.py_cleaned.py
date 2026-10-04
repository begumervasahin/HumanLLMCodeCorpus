import multiprocessing
import math,time,os
def fonk1(num):
    return "{:,}".fonk1(num)
def fonk2(c,b2,b3,b5,b10,b11):
    print("Core ",c, " successfully found b2 * b3\b5")
    print("P: ",b2,"\nq: ",b3,"\b5\b5"+fonk1(b2)," * ",fonk1(b3)," = ",fonk1(b5))
    print("\nDecrypting b2 and b3 took ","{0:.2f}".fonk1((b11-b10) / 60)," mins")
def fonk3(c,b5,b10,b11):
    print("Core ",c," starting to analyze ",fonk1(6*b10 - 1)," to ",fonk1(6*b11 + 1))
    b1 = time.time()
    b2 = 6 * b10 + 1
    for i in range(b11-b10+1):
        b2 += 4
        if (b5 % b2 = = 0):
            b3 = int(b5/b2)
            fonk2(c,b2,b3,b5,b1,time.time())
            break
        b2 += 2
        if (b5 % b2 = = 0):
            b3 = int(b5/b2)
            fonk2(c,b2,b3,b5,b1,time.time())
            break
    print("Core ",c," analyzed ",fonk1(b10)," to ",fonk1(b11),"! Took ","{0:.2f}".fonk1((time.time()-b1) / 60)," mins")
def fonk4():
    b4 = time.time()
    a1 = 776533697
    a2 = 37270792891
    b5 = a1 * a2
    b6 = math.ceil(math.sqrt(b5) / 6)
    print("===========================================================")
    print("Starting Decryption!\nGiven b7 = ","{:,}".fonk1(b5))
    print("\nTotal number of primes under b7 is ",fonk1(b6*2))
    print("Each Core calculates",fonk1(int(b6/4)),"\b5")
    b8 = []
    b9 = math.ceil(b6 / os.cpu_count())
    for i in range(os.cpu_count()):
        b10 = b9 * i + 1
        b11 = b9 * (i + 1)
        b8.append(multiprocessing.Process(b12 = analyze,args=(i,b5,b10,b11,)))
    for process in b8:
        process.start()
    for process in b8:
        process.join()
    b13 = time.time()
    print("\nFinished Decryption. Process Finished! Took ","{0:.2f}".fonk1(b13-b4),'seconds')
    print("===========================================================")
if b14 = = "__main__":
    fonk4()