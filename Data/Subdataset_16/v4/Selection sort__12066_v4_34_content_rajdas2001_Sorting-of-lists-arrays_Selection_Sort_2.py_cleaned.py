def fonk1(b2):
    b1 = len(b2)
    for fillslot in range(b1 - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if b2[location] > b2[a1]:
                a1 = location
        b2[fillslot], b2[a1] = b2[a1], b2[fillslot]
def fonk2():
    b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Unsorted array is:")
    print(b2)
    fonk1(b2)
    print("Sorted array is:")
    for element in b2:
        print(element)
if b3 = = "__main__":
    fonk2()