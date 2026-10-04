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
with open("NUM.txt", "r") as READ:
    b4 = READ.read()
    b5 = b4.split(" ")
    b5 = [int(i) for i in b5]
b6 = b5.copy()
b7 = time.process_time()
fonk1(b5)
b8 = time.process_time()
b9 = b8 - b7
b10 = time.process_time()
fonk2(b6)
b11 = time.process_time()
b12 = b11 - b10
with open("BUBBLE_SORTED.txt", "w") as WRITE_B:
    WRITE_B.write(" ".join(map(str, b5)) + "\b1")
    WRITE_B.write("Running time: " + str(b9) + " Seconds\b1")
with open("INSERTION_SORTED.txt", "w") as WRITE_I:
    WRITE_I.write(" ".join(map(str, b6)) + "\b1")
    WRITE_I.write("Running time: " + str(b12) + " Seconds\b1")