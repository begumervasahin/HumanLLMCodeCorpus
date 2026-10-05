
nums = []
with open("data.txt", "r") as file:
    for line in file:
        var = line.split(" ")
        nums.append(list(map(int, var[1:])))
print("Stooge Sort")
array_size = len(nums)
print("The unsorted arrays are: ")
for array in nums:
    print(array)
def stooge_sort(array, start, end):
    num_elms = end - start + 1
    if num_elms == 2:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    elif num_elms > 2:
        third = num_elms
        stooge_sort(array, start, end - third)
        stooge_sort(array, start + third, end)
        stooge_sort(array, start, end - third)
for array in nums:
    stooge_sort(array, 0, len(array) - 1)
print("The sorted arrays are: ")
for array in nums:
    print(array)
with open("stooge.out", "w") as file_out:
    for array in nums:
        file_out.write(" ".join(map(str, array)) + "\n")