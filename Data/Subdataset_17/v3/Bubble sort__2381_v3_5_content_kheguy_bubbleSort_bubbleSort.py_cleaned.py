import random
class BubbleSort:
    def __init__(self, size_of_array, interval_from, interval_to):
        self.array_size = size_of_array
        self.array = [random.randint(interval_from, interval_to) for _ in range(size_of_array)]
    def __del__(self):
        self.array.clear()
    def print_array(self):
        print(self.array)
    def sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(self.array_size - 1):
                if self.array[i + 1] < self.array[i]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    is_sorted = False
def get_user_input():
    while True:
        try:
            n = int(input('Enter size of array: '))
            a = int(input('Enter lower bound for random numbers: '))
            b = int(input('Enter upper bound for random numbers: '))
            if a > b:
                print("Invalid input: the lower bound should be less than or equal to the upper bound.")
                continue
            return n, a, b
        except ValueError:
            print("Invalid input. Please enter valid integers.")
def main():
    while True:
        n, a, b = get_user_input()
        sorter = BubbleSort(n, a, b)
        print("Original array:")
        sorter.print_array()
        sorter.sort()
        print("Sorted array:")
        sorter.print_array()
        del sorter
if __name__ == "__main__":
    main()