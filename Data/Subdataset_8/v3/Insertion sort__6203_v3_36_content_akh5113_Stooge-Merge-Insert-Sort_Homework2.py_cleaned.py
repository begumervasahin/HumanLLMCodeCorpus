def stooge_sort(arr, start, end):
    num_elms = end - start + 1
    if num_elms == 2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
    elif num_elms > 2:
        third = num_elms
        stooge_sort(arr, start, end - third)
        stooge_sort(arr, start + third, end)
        stooge_sort(arr, start, end - third)
nums = []
with open("data.txt", "r") as file:
    for line in file:
        var = line.split(" ")
        nums.append(list(map(int, var[1:])))
print("Stooge Sort")
print("The unsorted arrays are: ")
for arr in nums:
    print(arr)
for arr in nums:
    stooge_sort(arr, 0, len(arr) - 1)
print("The sorted arrays are: ")
for arr in nums:
    print(arr)
with open("stooge.out", "w") as f_out:
    for arr in nums:
        f_out.write(" ".join(map(str, arr)) + "\n")