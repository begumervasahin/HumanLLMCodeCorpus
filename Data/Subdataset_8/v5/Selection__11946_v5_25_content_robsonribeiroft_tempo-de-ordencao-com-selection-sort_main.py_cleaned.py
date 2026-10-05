import random
import timeit
import matplotlib.pyplot as plt
def generate_random_numbers(num_elements):
    random_numbers = []
    random.seed()
    for _ in range(num_elements):
        x = random.randint(1, 10 * num_elements)
        if x not in random_numbers:
            random_numbers.append(x)
    return random_numbers
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
if __name__ == "__main__":
    num_elements = [100, 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
    generation_times = []
    sorting_times = []
    for size in num_elements:
        generation_time = timeit.timeit(lambda: generate_random_numbers(size), number=1)
        generation_times.append(generation_time)
        random_list = generate_random_numbers(size)
        sorting_time = timeit.timeit(lambda: selection_sort(random_list.copy()), number=1)
        sorting_times.append(sorting_time)
        print(size)
    plt.plot(num_elements, generation_times, '*-', label='Generation Time')
    plt.plot(num_elements, sorting_times, 'o-', label='Sorting Time')
    plt.ylabel('Time (s)')
    plt.xlabel('Number of Elements')
    plt.legend()
    plt.show()