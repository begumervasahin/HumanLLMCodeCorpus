def fonk1(b2):
    for step in range(len(b2)):
        b1 = step
        for location in range(step, len(b2)):
            if b2[location] < b2[b1]:
                b1 = location
        b2[step], b2[b1] = b2[b1], b2[step]
    print("Sorted b2:", b2)
    print("Total number of b2:", len(b2))
b2 = [64, 25, 12, 22, 11]
fonk1(b2)