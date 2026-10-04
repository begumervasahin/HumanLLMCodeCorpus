import random
def generate_random_numbers():
    return random.sample(range(100001), 100)
def selection_sort(li):
    n = len(li)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
    return li
if __name__ == "__main__":
    random_numbers = generate_random_numbers()
    print("Unsorted list:")
    print(random_numbers)
    sorted_numbers = selection_sort(random_numbers)
    print("Sorted list:")
    print(sorted_numbers)