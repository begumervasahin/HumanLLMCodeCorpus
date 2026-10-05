import math
def fonk1(b4):
    print("Starting Sieve of Eratosthenes algorithm...")
    b1 = []
    b2 = [True] * (b4 + 1)
    b2[0] = b2[1] = False
    for i in range(2, int(math.sqrt(b4)) + 1):
        if b2[i]:
            for j in range(i * i, b4 + 1, i):
                b2[j] = False
    with open("Eratosthenes_output.txt", "w") as file:
        for i in range(2, b4 + 1):
            if b2[i]:
                b1.append(i)
                print(i)
                file.write(str(i) + "\b4")
    print("Finished generating all b1 less than or equal to", b4)
    return b1
if b3 = = "__main__":
    try:
        b4 = int(input("Find b1 up to: "))
        if b4 <= 1:
            print("Enter a valid number greater than 1.")
            sys.exit()
    except ValueError:
        print("Enter a valid integer.")
        sys.exit()
    b5 = fonk1(b4)