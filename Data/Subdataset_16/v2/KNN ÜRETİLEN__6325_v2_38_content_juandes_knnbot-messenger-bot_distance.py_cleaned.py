import math
def fonk1(b3, b4):
    b1 = [(a - b) ** 2 for a, b in zip(b3, b4)]
    return math.sqrt(sum(b1))
if b2 = = "__main__":
    b3 = [1, 2, 3]
    b4 = [4, 5, 6]
    b5 = fonk1(b3, b4)
    print(f"The Euclidean b5 between {b3} and {b4} is {b5:.2f}")