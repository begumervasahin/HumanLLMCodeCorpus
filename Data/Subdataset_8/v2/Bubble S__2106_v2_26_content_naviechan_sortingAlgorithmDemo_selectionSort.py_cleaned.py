class SelectionSort:
    def __init__(self, lst, trace_mode):
        self.lst = lst
        self.trace_mode = trace_mode
    def sort(self):
        lst = self.lst
        for start_idx in range(len(lst)):
            min_idx = self.find_min_index(start_idx)
            lst[start_idx], lst[min_idx] = lst[min_idx], lst[start_idx]
            if self.trace_mode:
                self.display_list(lst, start_idx, min_idx)
        return lst
    def find_min_index(self, start_idx):
        min_idx = start_idx
        for i in range(start_idx, len(self.lst)):
            if self.lst[i] < self.lst[min_idx]:
                min_idx = i
        return min_idx
    def display_list(self, lst, i, j):
        indicator_lst = ['*' if k == i or k == j else '' for k in range(len(lst))]
        output = '| ' + ' | '.join(str(elm) + indicator for elm, indicator in zip(lst, indicator_lst)) + ' |'
        print(output)
        input("Press Enter to continue...")
def main():
    input_list = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    trace_mode = True
    sorter = SelectionSort(input_list, trace_mode)
    sorted_list = sorter.sort()
    print("Sorted list:", sorted_list)
if __name__ == "__main__":
    main()