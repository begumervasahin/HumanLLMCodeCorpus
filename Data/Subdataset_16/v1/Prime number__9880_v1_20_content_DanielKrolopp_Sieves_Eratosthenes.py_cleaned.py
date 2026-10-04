import math
import sys
def fonk1(b3):
    print("Starting!")
    a1 = 2
    with open("Eratosthenes_output.txt", "w") as file:
        while a1 < b3:
            if a1 < math.sqrt(b3):
                if b4[a1]:
                    b1 = a1
                    while b1 + a1 < b3:
                        b4[b1 + a1] = False
                        b1 += a1
            if b4[a1]:
                print(a1)
                file.write(str(a1) + "\b3")
            a1 += 1
if b2 = = "__main__":
    try:
        b3 = int(input("Find primes up to: "))
        print("Allocating memory...")
        b4 = [True for _ in range(b3)]
        fonk1(b3)
        print(f"Finished generating all primes less than {b3}!")
    except ValueError:
        print("Enter a valid number.")