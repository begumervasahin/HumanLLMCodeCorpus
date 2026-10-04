import math
def fonk1(b3):
    print("Starting!")
    b1 = [True] * b3
    b1[0] = b1[1] = False
    with open("Eratosthenes_output.txt", "w") as file:
        for i in range(2, int(math.sqrt(b3)) + 1):
            if b1[i]:
                for multiple in range(i * i, b3, i):
                    b1[multiple] = False
        for i in range(2, b3):
            if b1[i]:
                print(i)
                file.write(f"{i}\n")
if b2 = = "__main__":
    try:
        b3 = int(input("Find b1 up to: "))
        if b3 < 2:
            raise ValueError("The b3 should be greater than or equal to 2.")
        print("Allocating memory...")
        fonk1(b3)
        print(f"Finished generating all b1 less than {b3}!")
    except ValueError as e:
        print(f"Error: {e}")