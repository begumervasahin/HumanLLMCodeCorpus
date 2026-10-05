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