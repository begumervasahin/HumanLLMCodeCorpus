import random
def generate_random_numbers():
    return random.sample(range(100001), 100)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
def main():
    random_numbers = generate_random_numbers()
    print("Unsorted list:")
    print(random_numbers)
    sorted_numbers = selection_sort(random_numbers)
    print("Sorted list:")
    print(sorted_numbers)
if __name__ == "__main__":
    main()