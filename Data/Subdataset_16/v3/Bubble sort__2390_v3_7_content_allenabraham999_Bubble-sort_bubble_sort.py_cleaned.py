import random
def fonk1(b2):
    b1 = len(b2)
    for j in range(b1):
        for i in range(1, b1):
            if b2[i - 1] > b2[i]:
                b2[i - 1], b2[i] = b2[i], b2[i - 1]
        print(f"\nArray after {j + 1} pass:")
        fonk2(b2)
def fonk2(b2):
    print(" ".join(map(str, b2)))
def fonk3(size, lower_bound, upper_bound):
    b2 = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    print("The b3 that will be worked on is:")
    fonk2(b2)
    return b2
def fonk4():
    b3 = fonk3(8, 1, 9)
    print()
    fonk1(b3)
    print("\nThe final sorted b3 is:")
    fonk2(b3)
if b4 = = "__main__":
    fonk4()