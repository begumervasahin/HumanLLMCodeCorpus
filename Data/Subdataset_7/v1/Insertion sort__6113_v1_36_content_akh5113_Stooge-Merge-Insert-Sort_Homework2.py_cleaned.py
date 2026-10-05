def fonk1(arr, start, end):
    b1 = (end - start + 1)
    if b1 = = 2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
    if b1 > 2:
        b2 = int(b1 / 3)
        fonk1(arr, start, end - b2)
        fonk1(arr, start + b2, end)
        fonk1(arr, start, end - b2)
b3 = []
with open("data.txt", "r") as f:
    for line in f:
        b4 = line.split(" ")
        b3.append(list(map(int, b4[1:])))
print("Merge Sort")
b5 = len(b3)
print("The unsorted arrays are: ")
for arr in b3:
    print(arr)
for arr in b3:
    fonk1(arr, 0, len(arr) - 1)
print("The sorted arrays are: ")
for arr in b3:
    print(arr)
with open("stooge.out", "w") as f_out:
    for arr in b3:
        f_out.write(" ".join(map(str, arr)) + "\n")