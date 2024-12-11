import random
import time
def fonk1(filename, n):
    random.seed(0)
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(str(random.randrange(0, 100)) + "\n")
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
    with open(input_file, 'r') as f:
        b8 = [int(line.strip()) for line in f]
    b9 = time.time() - b7
    print(f"It took {b9:.6f} seconds to input b8 from file {input_file}")
    b10 = sorting_algorithm(b8)
    b11 = time.time() - b7 - b9
    print(f"It took {b11:.6f} seconds to sort {len(b8)} b8 using {sorting_algorithm.b14}")
    with open(output_file, 'w') as f:
        for value in b10:
            f.write(f"{value}\n")
    b12 = time.time() - b7 - b9 - b11
    print(f"It took {b12:.6f} seconds to output {len(b8)} sorted b8 to file {output_file}")
    b13 = time.time() - b7
    print(f"Total time the program took is {b13:.6f} seconds\n")
if b14 = = '__main__':
    b15 = input("Enter the filename: ")
    b16 = int(input("Enter number of b8: "))
    fonk1(b15, b16)
    b17 = input("Please enter output file name: ")
    fonk5(b15, b17, merge_sort)
    fonk5(b15, b17, selection_sort)