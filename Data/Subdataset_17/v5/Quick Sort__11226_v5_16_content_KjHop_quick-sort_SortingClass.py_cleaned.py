class Sorting:
    def __init__(self):
        self.list_of_numbers = []
    def add_number(self, number):
        self.list_of_numbers.append(number)
    def get_list(self):
        return self.list_of_numbers
    def print_list(self):
        for number in self.list_of_numbers:
            print(number)
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)
        less_than_pivot = [number for number in arr if number < pivot]
        equal_to_pivot = [number for number in arr if number == pivot]
        greater_than_pivot = [number for number in arr if number > pivot]
        return self.quick_sort(less_than_pivot) + equal_to_pivot + self.quick_sort(greater_than_pivot)
if __name__ == "__main__":
    sorting = Sorting()
    numbers_to_add = [3, 6, 8, 10, 1, 2, 1]
    for number in numbers_to_add:
        sorting.add_number(number)
    print("Original List:")
    sorting.print_list()
    sorted_list = sorting.quick_sort(sorting.get_list())
    print("\nSorted List:")
    for num in sorted_list:
        print(num)