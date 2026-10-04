import random
def generate_random_numbers(count=100, upper_limit=100000):
    return random.sample(range(upper_limit + 1), count)
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
    random_list = generate_random_numbers()
    print("Original list:")
    print(random_list)
    sorted_list = selection_sort(random_list)
    print("Sorted list:")
    print(sorted_list)
if __name__ == "__main__":
    main()