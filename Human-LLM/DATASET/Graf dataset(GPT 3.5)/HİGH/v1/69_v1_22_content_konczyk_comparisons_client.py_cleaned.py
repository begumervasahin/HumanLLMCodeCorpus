def fonk1(arr, low, high):
    return low
def fonk2(arr, low, high):
    return high
def fonk3(arr, low, high):
    b1 = (low + high)
    if arr[low] < arr[b1] < arr[high] or arr[high] < arr[b1] < arr[low]:
        return b1
    elif arr[b1] < arr[low] < arr[high] or arr[high] < arr[low] < arr[b1]:
        return low
    else:
        return high