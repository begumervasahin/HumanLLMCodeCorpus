def fonk1(b1, val):
    while val in b1:
        b1.remove(val)
        print(f"Current list after removing {val}: {b1}")
    return b1
b1 = [3, 2, 2, 3]
print(f"After removing 2: {fonk1(b1, 2)}")
b1 = [1, 2, 3, 4, 2, 2, 5]
print(f"After removing 2: {fonk1(b1, 2)}")
b1 = [4, 4, 4, 4]
print(f"After removing 4: {fonk1(b1, 4)}")
b1 = [1, 2, 3, 4, 5]
print(f"After removing 6: {fonk1(b1, 6)}")
