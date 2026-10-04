
def fonk1(input_list):
    b1 = list(input_list)
    b2 = []
    while b1:
        b3 = b1[0]
        for element in b1:
            if element < b3:
                b3 = element
        b2.append(b3)
        b1.remove(b3)
    return b2
if b4 = = "__main__":
    b5 = [34, 23, 12, 45, 9, 1, 24]
    print("Original list:", b5)
    b6 = fonk1(b5)
    print("Sorted list:", b6)