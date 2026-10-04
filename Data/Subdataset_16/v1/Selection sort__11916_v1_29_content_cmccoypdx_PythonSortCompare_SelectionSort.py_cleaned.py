def fonk1(input_list):
    b1 = list(input_list)
    b2 = []
    while b1:
        b3 = b1[0]
        for item in b1:
            if item < b3:
                b3 = item
        b2.append(b3)
        b1.remove(b3)
    return b2
if b4 = = "__main__":
    b5 = [64, 25, 12, 22, 11]
    b2 = fonk1(b5)
    print("Original list:", b5)
    print("Sorted list:", b2)