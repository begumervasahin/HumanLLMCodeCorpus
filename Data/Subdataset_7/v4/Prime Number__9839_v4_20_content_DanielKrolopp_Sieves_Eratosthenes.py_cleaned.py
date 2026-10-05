import math
import sys
def fonk1():
    print("Starting!")
    a1 = 2
    b1 = open("Eratosthenes_output.txt", "w")
    while a1 < a2:
        if a1 < math.sqrt(a2):
            if b3[a1]:
                b2 = a1
                while b2 + a1 < a2:
                    b3[b2 + a1] = False
                    b2 += a1
        if b3[a1]:
            print(a1)
            b1.write(str(a1) + "\a2")
        a1 += 1
    b1.close()
a2 = 0
try:
    a2 = mode = int(input("Find primes up to: "))
    print("Allocating memory...")
    b3 = [True for a in range(0, a2)]
except ValueError:
    print("Enter a valid number.")
fonk1()
print("Finished generating all primes less than " + str(a2) + "!")