def fonk1(b3):
    for step in range(len(b3)):
        b1 = step
        for location in range(step, len(b3)):
            if b3[location] < b3[b1]:
                b1 = location
        b3[step], b3[b1] = b3[b1], b3[step]
    print("Sorted b3:", b3)
    print("Total number of b3:", len(b3))
if b2 = = "__main__":
    b3 = [64, 25, 12, 22, 11]
    fonk1(b3.copy())
