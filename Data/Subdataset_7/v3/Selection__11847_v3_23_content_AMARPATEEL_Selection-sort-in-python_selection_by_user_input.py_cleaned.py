def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        for j in range(i + 1, len(b2)):
            if b2[b1] > b2[j]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
def fonk2():
    b2 = []
    b3 = int(input("Enter the number of elements in the list: "))
    for _ in range(b3):
        b4 = int(input("Enter an b4: "))
        b2.append(b4)
    return b2
if b5 = = "__main__":
    b2 = fonk2()
    print("List before sorting:", b2)
    fonk1(b2)
    print("List after sorting:", b2)