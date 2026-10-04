class SelectionSort:
    def __init__(self, lst, trace_mode=False):
        self.lst = lst
        self.trace_mode = trace_mode
    def sort(self):
        for start_idx in range(len(self.lst)):
            min_idx = start_idx
            for i in range(start_idx + 1, len(self.lst)):
                if self.lst[i] < self.lst[min_idx]:
                    min_idx = i
            self.lst[start_idx], self.lst[min_idx] = self.lst[min_idx], self.lst[start_idx]
            if self.trace_mode:
                self.display_list(start_idx, min_idx)
        return self.lst
    def display_list(self, i, j):
        lst_str = [f"{elm}*" if idx == i or idx == j else str(elm) for idx, elm in enumerate(self.lst)]
        output = '| ' + ' | '.join(lst_str) + ' |'
        print(output)
        input("Press Enter to continue...")
if __name__ == "__main__":
    lst = [64, 25, 12, 22, 11]
    sorter = SelectionSort(lst, trace_mode=True)
    sorted_lst = sorter.sort()
    print("Sorted list:", sorted_lst)