import random
import time
def fonk1(filename, n):
    random.seed(0)
    with open(filename, 'w') as file:
        for _ in range(n):
            file.write(f"{random.randrange(0, 100)}\n")
def fonk2(b4, b5):
    b1 = []
    left_index, b2 = 0, 0
    while left_index < len(b4) and b2 < len(b5):
        if b4[left_index] < b5[b2]:
            b1.append(b4[left_index])
            left_index += 1
        else:
            b1.append(b5[b2])
            b2 += 1
    b1.extend(b4[left_index:])
    b1.extend(b5[b2:])
    return b1
def fonk3(arr):
    if len(arr) <= 1:
        return arr
    else:
        b3 = len(arr)
        b4 = fonk3(arr[:b3])
        b5 = fonk3(arr[b3:])
        return fonk2(b4, b5)
def fonk4(arr):
    for i in range(len(arr) - 1):
        b6 = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[b6]:
                b6 = j
        arr[i], arr[b6] = arr[b6], arr[i]
    return arr
def fonk5(input_file, output_file, sorting_algorithm):
    b7 = time.time()
    with open(input_file, 'r') as file:
        b8 = [int(line.strip()) for line in file]
    b9 = time.time() - b7
    print(f"Input time: {b9:.6f} seconds")
    b10 = sorting_algorithm(b8)
    b11 = time.time() - b7 - b9
    print(f"Sorting time: {b11:.6f} seconds")
    with open(output_file, 'w') as file:
        for value in b10:
            file.write(f"{value}\n")
    b12 = time.time() - b7 - b9 - b11
    print(f"Output time: {b12:.6f} seconds")
    b13 = time.time() - b7
    print(f"Total time: {b13:.6f} seconds\n")
if b14 = = '__main__':
    b15 = input("Enter the filename: ")
    b16 = int(input("Enter number of b8: "))
    fonk1(b15, b16)
    b17 = input("Please enter output file name: ")
    fonk5(b15, b17, merge_sort)
    fonk5(b15, b17, selection_sort)