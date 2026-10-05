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
        less_than_pivot = []
        equal_pivot = []
        greater_than_pivot = []
        if len(arr) > 1:
            pivot = arr[-1]
            for number in arr:
                if number < pivot:
                    less_than_pivot.append(number)
                elif number == pivot:
                    equal_pivot.append(number)
                else:
                    greater_than_pivot.append(number)
            return self.quick_sort(less_than_pivot) + equal_pivot + self.quick_sort(greater_than_pivot)
        else:
            return arr
sorting = Sorting()
sorting.add_number(3)
sorting.add_number(1)
sorting.add_number(5)
sorting.add_number(2)
sorting.add_number(4)
print("Original list:", sorting.return_list())
sorted_list = sorting.quick_sort(sorting.return_list())
print("Sorted list:", sorted_list)