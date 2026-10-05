def fonk1(num_list):
    b1 = []
    while num_list:
        b2 = min(num_list)
        b1.append(b2)
        num_list.remove(b2)
        fonk2(b1, num_list)
    print("\nSorted list:", b1)
def fonk2(b1, remaining_list):
    print("\nStep", len(b1))
    print("Remaining:", remaining_list)
    print("Sorted:", b1)
b3 = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
fonk1(b3)