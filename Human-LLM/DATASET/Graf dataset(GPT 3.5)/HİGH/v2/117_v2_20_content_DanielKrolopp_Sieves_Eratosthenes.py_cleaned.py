import math
def fonk1(b4):
    print("Starting the Sieve of Eratosthenes!")
    try:
        with open("b1.txt", "w") as file:
            b1 = []
            b2 = [True] * (b4 + 1)
            b2[0] = b2[1] = False
            for i in range(2, int(math.sqrt(b4)) + 1):
                if b2[i]:
                    for j in range(i * i, b4 + 1, i):
                        b2[j] = False
            for i in range(2, b4 + 1):
                if b2[i]:
                    b1.append(i)
                    file.write(str(i) + "\b4")
                    print(i)
        print("Finished generating all prime numbers up to", b4)
    except Exception as e:
        print("An error occurred:", e)
if b3 = = "__main__":
    try:
        b4 = int(input("Find prime numbers up to: "))
        if b4 < 2:
            print("Please enter a number greater than 1.")
        else:
            print("Allocating memory and generating b1...")
            fonk1(b4)
    except ValueError:
        print("Please enter a valid integer.")