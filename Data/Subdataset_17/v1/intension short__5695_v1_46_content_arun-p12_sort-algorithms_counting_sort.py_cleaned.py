def counting_sort(arr, verbose=0, desc=False):
    largest = max(arr)
    smallest = min(arr)
    if smallest < 0:
        arr = [x - smallest for x in arr]
    if verbose:
        print("Normalized array:", arr)
    range_of_elements = largest - smallest + 1
    count = [0] * range_of_elements
    for number in arr:
        count[number] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        if verbose == 2:
            print(f"Count after processing index {i}: {count}")
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        current_number = arr[i]
        count[current_number] -= 1
        output[count[current_number]] = current_number
    if smallest < 0:
        output = [x + smallest for x in output]
    if desc:
        output = output[::-1]
    return output
if __name__ == "__main__":
    A = [4, 2, 2, 8, 3, 3, 1]
    sorted_A = counting_sort(A, verbose=1, desc=False)
    print("Sorted array:", sorted_A)