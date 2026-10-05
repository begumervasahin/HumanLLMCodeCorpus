import math
class SelectionSort:
    def __init__(self, lst, trace_mode):
        self.lst = lst
        self.trace_mode = trace_mode
    def sort(self):
        lst = self.lst
        for start_idx in range(len(lst)):
            min_val = lst[start_idx]
            min_idx = start_idx
            for i in range(start_idx + 1, len(lst)):
                if lst[i] < min_val:
                    min_val = lst[i]
                    min_idx = i
            lst[start_idx], lst[min_idx] = lst[min_idx], lst[start_idx]
            if self.trace_mode:
                self.display_list(start_idx, min_idx)
        return lst
    def display_list(self, i, j):
        lst = [str(elm) + '*' if idx in (i, j) else str(elm) for idx, elm in enumerate(self.lst)]
        output = '|' + ' | '.join(lst) + ' |'
        print(output)
        input("Press Enter to continue...")