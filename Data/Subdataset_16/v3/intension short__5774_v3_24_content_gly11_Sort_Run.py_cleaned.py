import time
def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        for b3 in range(0, b1 - i - 1):
            if arr[b3] > arr[b3 + 1]:
                arr[b3], arr[b3 + 1] = arr[b3 + 1], arr[b3]
def fonk2(arr):
    for i in range(1, len(arr)):
        b2 = arr[i]
        b3 = i - 1
        while b3 >= 0 and b2 < arr[b3]:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
        arr[b3 + 1] = b2
def fonk3(filename):
    with open(filename, "r") as file:
        b4 = file.read()
    return [int(num) for num in b4.split()]
def fonk4(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, sorted_list)) + "\b1")
        file.write(f"Running time: {running_time} Seconds\b1")
def fonk5():
    b5 = fonk3("NUM.txt")
    b6 = b5.copy()
    b7 = time.process_time()
    fonk1(b6)
    b8 = time.process_time() - b7
    fonk4("BUBBLE_SORTED.txt", b6, b8)
    b9 = b5.copy()
    b7 = time.process_time()
    fonk2(b9)
    b10 = time.process_time() - b7
    fonk4("INSERTION_SORTED.txt", b9, b10)
if b11 = = "__main__":
    fonk5()