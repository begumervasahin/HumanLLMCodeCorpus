def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        for j in range(i + 1, len(b2)):
            if b2[j] < b2[b1]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
def fonk2():
    b2 = [49, 25, 26, 2, 99]
    print("Original array:", b2)
    fonk1(b2)
    print("Sorted array is:")
    for element in b2:
        print(element, b3 = ' ')
if b4 = = "__main__":
    fonk2()