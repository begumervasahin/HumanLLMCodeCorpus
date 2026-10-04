def fonk1(arr):
    for fillslot in range(len(arr) - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if arr[location] > arr[a1]:
                a1 = location
        arr[fillslot], arr[a1] = arr[a1], arr[fillslot]
if b1 = = "__main__":
    b2 = [54, 45, 67, 12, 34, 98, 66]
    print("List before sorting:", b2)
    fonk1(b2)
    print("List after sorting:", b2)