import random
class BubbleSort:
    def __init__(self, size_of_array, interval_from, interval_to):
        self.array_size = size_of_array
        self.array = []
        i = 0
        random.seed()
        while i < self.array_size:
            self.array.insert(i, random.randint(interval_from, interval_to))
            i += 1
    def __del__(self):
        self.array.clear()
    def print_array(self):
        print(self.array)
    def sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            i = 0
            while i < self.array_size - 1:
                if self.array[i + 1] < self.array[i]:
                    self.array[i + 1], self.array[i] = self.array[i], self.array[i + 1]
                    is_sorted = False
                i += 1
def main():
    while True:
        n = int(input('Enter size of array:\n'))
        a = int(input('Enter primary position for random:\n'))
        b = int(input('Enter final position for random:\n'))
        sort = BubbleSort(n, a, b)
        sort.print_array()
        sort.sort()
        sort.print_array()
        del sort
if __name__ == "__main__":
    main()