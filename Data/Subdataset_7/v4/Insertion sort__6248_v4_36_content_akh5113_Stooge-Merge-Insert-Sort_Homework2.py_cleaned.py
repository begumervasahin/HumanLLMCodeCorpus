
b1 = []
with open("data.txt", "r") as file:
    for line in file:
        b2 = line.split(" ")
        b1.append(list(map(int, b2[1:])))
print("Stooge Sort")
b3 = len(b1)
print("The unsorted arrays are: ")
for array in b1:
    print(array)
def fonk1(array, start, end):
    b4 = end - start + 1
    if b4 = = 2:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    elif b4 > 2:
        b5 = b4
        fonk1(array, start, end - b5)
        fonk1(array, start + b5, end)
        fonk1(array, start, end - b5)
for array in b1:
    fonk1(array, 0, len(array) - 1)
print("The sorted arrays are: ")
for array in b1:
    print(array)
with open("stooge.out", "w") as file_out:
    for array in b1:
        file_out.write(" ".join(map(str, array)) + "\n")