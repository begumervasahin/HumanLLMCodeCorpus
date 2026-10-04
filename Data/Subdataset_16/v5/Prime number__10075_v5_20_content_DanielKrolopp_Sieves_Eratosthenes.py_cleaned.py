import math
def fonk1(b2):
    print("Starting!")
    b1 = [True] * (b2 + 1)
    b1[0] = b1[1] = False
    with open("Eratosthenes_output.txt", "w") as file:
        for i in range(2, int(math.sqrt(b2)) + 1):
            if b1[i]:
                for j in range(i * i, b2 + 1, i):
                    b1[j] = False
        for i in range(2, b2 + 1):
            if b1[i]:
                print(i)
                file.write(f"{i}\b2")
    print(f"Finished generating all b1 up to {b2}!")
def fonk2():
    try:
        b2 = int(input("Find b1 up to: "))
        if b2 < 2:
            raise ValueError("Number must be greater than or equal to 2.")
        print("Allocating memory...")
        fonk1(b2)
    except ValueError as e:
        print(f"Error: {e}")
if b3 = = "__main__":
    fonk2()