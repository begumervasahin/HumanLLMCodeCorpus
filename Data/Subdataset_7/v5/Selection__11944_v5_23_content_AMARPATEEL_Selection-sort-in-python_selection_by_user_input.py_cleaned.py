def fonk1(b2, start):
    b1 = start
    for i in range(start + 1, len(b2)):
        if b2[i] < b2[b1]:
            b1 = i
    return b1
def fonk2(b2):
    for i in range(len(b2)):
        b1 = fonk1(b2, i)
        b2[i], b2[b1] = b2[b1], b2[i]
b2 = []
b3 = int(input("Number of elements in the list: "))
for i in range(b3):
    b4 = int(input("Enter an element: "))
    b2.append(b4)
print("List before sorting:", b2)
fonk2(b2)
print("List after sorting:", b2)