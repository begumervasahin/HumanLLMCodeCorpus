class Sorting:
    def __init__(self):
        self.numbers = []
    def add_number(self, number):
        self.numbers.append(number)
    def get_numbers(self):
        return self.numbers
    def print_numbers(self):
        for number in self.numbers:
            print(number)
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[-1]
            less_than_pivot = [num for num in arr if num < pivot]
            equal_to_pivot = [num for num in arr if num == pivot]
            greater_than_pivot = [num for num in arr if num > pivot]
            return self.quick_sort(less_than_pivot) + equal_to_pivot + self.quick_sort(greater_than_pivot)
if __name__ == "__main__":
    sorting = Sorting()
    numbers_to_add = [34, 7, 23, 32, 5, 62, 32, 7]
    for number in numbers_to_add:
        sorting.add_number(number)
    print("Original list:")
    sorting.print_numbers()
    sorted_list = sorting.quick_sort(sorting.get_numbers())
    print("\nSorted list:")
    for number in sorted_list:
        print(number)