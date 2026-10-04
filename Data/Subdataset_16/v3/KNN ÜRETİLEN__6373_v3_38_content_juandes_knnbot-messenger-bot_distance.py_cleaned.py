import math
def fonk1(b2, b3):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(b2, b3)))
if b1 = = "__main__":
    b2 = [1.0, 2.0, 3.0]
    b3 = [4.0, 5.0, 6.0]
    b4 = fonk1(b2, b3)
    print(f"The Euclidean b4 between {b2} and {b3} is {b4:.2f}")