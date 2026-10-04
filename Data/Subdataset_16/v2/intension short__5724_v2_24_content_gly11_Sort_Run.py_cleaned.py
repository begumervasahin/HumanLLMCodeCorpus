import time
def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        for b3 in range(0, b1-i-1):
            if arr[b3] > arr[b3+1]:
                arr[b3], arr[b3+1] = arr[b3+1], arr[b3]
def fonk2(arr):
    for i in range(1, len(arr)):
        b2 = arr[i]
        b3 = i-1
        while b3 >= 0 and b2 < arr[b3]:
            arr[b3+1] = arr[b3]
            b3 -= 1
        arr[b3+1] = b2
with open("NUM.txt", "r") as file:
    b4 = file.read()
    b5 = [int(num) for num in b4.split()]
b6 = b5.copy()
b7 = time.process_time()
fonk1(b5)
b8 = time.process_time()
b9 = b8 - b7
b10 = time.process_time()
fonk2(b6)
b11 = time.process_time()
b12 = b11 - b10
with open("BUBBLE_SORTED.txt", "w") as file_bubble:
    file_bubble.write(" ".join(map(str, b5)) + "\b1")
    file_bubble.write(f"Running time: {b9} Seconds\b1")
with open("INSERTION_SORTED.txt", "w") as file_insertion:
    file_insertion.write(" ".join(map(str, b6)) + "\b1")
    file_insertion.write(f"Running time: {b12} Seconds\b1")