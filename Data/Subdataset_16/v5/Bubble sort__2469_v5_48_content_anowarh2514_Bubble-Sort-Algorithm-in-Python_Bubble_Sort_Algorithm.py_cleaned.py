def fonk1(b4):
    b1 = len(b4)
    for i in range(b1 - 1):
        b2 = False
        for j in range(b1 - 1 - i):
            if b4[j] > b4[j + 1]:
                b4[j], b4[j + 1] = b4[j + 1], b4[j]
                b2 = True
        print(f"After pass {i + 1}: {b4}")
        if not b2:
            break
if b3 = = "__main__":
    b4 = [5, 3, 8, 6, 7, 2]
    print("Unsorted List:", b4)
    fonk1(b4)
    print("Sorted List:", b4)