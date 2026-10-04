class SelectionSort:
    def __init__(self, lst, trace_mode):
        self.lst = lst
        self.trace_mode = trace_mode
    def sort(self):
        lst = self.lst
        for start_idx in range(len(lst)):
            min_idx = start_idx
            for i in range(start_idx + 1, len(lst)):
                if lst[i] < lst[min_idx]:
                    min_idx = i
            lst[start_idx], lst[min_idx] = lst[min_idx], lst[start_idx]
            if self.trace_mode:
                self.display_list(lst, start_idx, min_idx)
        return lst
    def display_list(self, lst, i, j):
        output = '|'
        for k, elm in enumerate(lst):
            marker = '*' if k == i or k == j else ''
            output += f' {elm}{marker} |'
        print(output)
        input("Press Enter to continue...")
def main():
    trace_mode = True
    lst = [64, 25, 12, 22, 11]
    sorter = SelectionSort(lst, trace_mode)
    sorted_list = sorter.sort()
    print('Sorted List:', sorted_list)
if __name__ == "__main__":
    main()