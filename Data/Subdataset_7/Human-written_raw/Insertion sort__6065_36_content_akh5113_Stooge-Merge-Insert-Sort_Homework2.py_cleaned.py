import math
b1 = []
with open("data.txt", "r") as f:
    for x in f:
        b2 = x.split(" ")
        for y in range(len(b2)):
            b2[y] = int(b2[y])
        b1.append(b2[1:])
f.close()
print("Merge Sort")
b3 = len(b1)
print("The unsorted arrays are: ")
for a in range(b3):
    print(b1[a])
def fonk1(array, start, end):
    b4 = (end - start + 1)
    if b4 = = 2:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    if b4 > 2:
        b5 = int(b4/3)
        fonk1(array, start, (end - b5))
        fonk1(array, (start + b5), end)
        fonk1(array, start, (end - b5))
for listS in b1:
    fonk1(listS, 0, (len(listS)-1))
print("The sorted arrays are: ")
for i in range(b3):
    print(b1[i])
b6 = open("stooge.out", "w+")
for nLine in range(b3):
    b7 = b1[nLine]
    for x in range(len(b7)):
        b6.write(str(b7[x]))
        b6.write(" ")
    b6.write("\n")
b6.close()