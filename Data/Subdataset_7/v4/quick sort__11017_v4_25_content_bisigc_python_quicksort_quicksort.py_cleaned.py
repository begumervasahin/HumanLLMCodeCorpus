def fonk1(arr, left, right):
    if left < right:
        b1 = arr[left]
        b2 = left
        for i in range(left + 1, right):
            if arr[i] < b1:
                b2 += 1
                arr[b2], arr[i] = arr[i], arr[b2]
        arr[left], arr[b2] = arr[b2], arr[left]
        fonk1(arr, left, b2 - 1)
        fonk1(arr, b2 + 1, right)