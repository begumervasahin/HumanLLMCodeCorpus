class BubbleSort:
    def __init__(self, lst, trace_mode=False):
        self.lst = lst
        self.trace_mode = trace_mode
    def sort(self):
        sorted = False
        lst = self.lst
        while not sorted:
            sorted = True
            for i in range(len(lst) - 1):
                j = i + 1
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    sorted = False
                if self.trace_mode:
                    self.display_list(lst, i, j)
        return lst
    @staticmethod
    def display_list(lst, i, j):
        lst_with_markers = [f"{elm}*" if k in (i, j) else elm for k, elm in enumerate(lst)]
        output = ' | '.join(map(str, lst_with_markers))
        print(output)
        input("Press Enter to continue...")
def main():
    input_list = [64, 25, 12, 22, 11]
    trace_mode = True
    sorter = BubbleSort(input_list, trace_mode)
    sorted_list = sorter.sort()
    print("Sorted array:", sorted_list)
if __name__ == "__main__":
    main()