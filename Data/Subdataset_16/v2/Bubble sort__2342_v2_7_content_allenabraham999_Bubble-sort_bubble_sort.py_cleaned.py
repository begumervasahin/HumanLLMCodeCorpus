import random
def fonk1(b3):
    b1 = len(b3)
    for j in range(b1):
        for i in range(1, b1):
            if b3[i - 1] > b3[i]:
                b3[i - 1], b3[i] = b3[i], b3[i - 1]
        print(f"\nArray after {j + 1} pass:")
        fonk2(b3)
def fonk2(b3):
    for element in b3:
        print(element, b2 = " ")
    print()
def fonk3(size, lower_bound, upper_bound):
    b3 = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    print("The b4 that will be worked on is:")
    fonk2(b3)
    return b3
def fonk4():
    b4 = fonk3(8, 1, 9)
    print()
    fonk1(b4)
    print("\nThe final sorted b4 is:")
    fonk2(b4)
if b5 = = "__main__":
    fonk4()