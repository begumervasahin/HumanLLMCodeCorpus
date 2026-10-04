class Sorting:
    def __init__(self):
        self.list_of_numbers = []
    def add_number(self, number):
        self.list_of_numbers.append(number)
    def return_list(self):
        return self.list_of_numbers
    def print_each_element_of_list(self):
        for number in self.list_of_numbers:
            print(number)
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) - 1]
        less_than_pivot = [number for number in arr if number < pivot]
        equal_to_pivot = [number for number in arr if number == pivot]
        greater_than_pivot = [number for number in arr if number > pivot]
        return self.quick_sort(less_than_pivot) + equal_to_pivot + self.quick_sort(greater_than_pivot)
if __name__ == "__main__":
    sorting = Sorting()
    sorting.add_number(3)
    sorting.add_number(6)
    sorting.add_number(8)
    sorting.add_number(10)
    sorting.add_number(1)
    sorting.add_number(2)
    sorting.add_number(1)
    print("Original List:")
    sorting.print_each_element_of_list()
    sorted_list = sorting.quick_sort(sorting.return_list())
    print("\nSorted List:")
    for num in sorted_list:
        print(num)