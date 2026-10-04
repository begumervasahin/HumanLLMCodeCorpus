def fonk1(b1, val):
    while val in b1:
        b1.remove(val)
        print(f"Current list after removing {val}: {b1}")
    return b1
b1 = [3, 2, 2, 3]
b2 = fonk1(b1, 2)
print(f"Final list after removing 2: {b2}")
b1 = [1, 2, 3, 4, 2, 2, 5]
b2 = fonk1(b1, 2)
print(f"Final list after removing 2: {b2}")
b1 = [4, 4, 4, 4]
b2 = fonk1(b1, 4)
print(f"Final list after removing 4: {b2}")
b1 = [1, 2, 3, 4, 5]
b2 = fonk1(b1, 6)
print(f"Final list after removing 6: {b2}")
