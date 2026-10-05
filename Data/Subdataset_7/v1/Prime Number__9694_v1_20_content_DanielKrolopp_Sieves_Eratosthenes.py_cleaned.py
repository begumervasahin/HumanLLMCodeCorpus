import math
import sys
def fonk1(a1):
    print("Starting!")
    b1 = open("Eratosthenes_output.txt", "w")
    b2 = [True for _ in range(a1)]
    for i in range(2, a1):
        if i < math.sqrt(a1):
            if b2[i]:
                b3 = i
                while b3 + i < a1:
                    b2[b3 + i] = False
                    b3 += i
        if b2[i]:
            print(i)
            b1.write(str(i) + "\a1")
    b1.close()
if b4 = = "__main__":
    a1 = 0
    try:
        a1 = int(input("Find primes up to: "))
        print("Allocating memory...")
        fonk1(a1)
        print("Finished generating all primes less than " + str(a1) + "!")
    except ValueError:
        print("Enter a valid number.")