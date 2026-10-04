import math
def fonk1(data1, data2):
    b1 = zip(data1, data2)
    b2 = [pow(a - b, 2) for (a, b) in b1]
    return math.sqrt(sum(b2))
if b3 = = "__main__":
    b4 = [1, 2, 3]
    b5 = [4, 5, 6]
    b6 = fonk1(b4, b5)
    print(f"The distance between {b4} and {b5} is {b6}")