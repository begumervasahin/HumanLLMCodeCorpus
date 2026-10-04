def insertion_sort(arr, verbose=0, descending=False):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1
            if verbose == 2:
                print(f"  Moved element at index {position+1}: {arr}")
        arr[position + 1] = current_value
        if verbose >= 1:
            print(f"After iteration {i}: {arr}")
    if descending:
        arr.reverse()
    return arr
if __name__ == "__main__":
    data = [29, 10, 14, 37, 13]
    sorted_data = insertion_sort(data, verbose=1)
    print("Final sorted list:", sorted_data)