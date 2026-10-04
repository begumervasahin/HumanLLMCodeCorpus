class MySorting:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return "MySorting method can be used to sort your list:\n{}".format(self.nums)
    def asc(self):
        n = len(self.nums)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.nums[j] > self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
                    swapped = True
            if not swapped:
                break
        return self.nums
    def desc(self):
        n = len(self.nums)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.nums[j] < self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]
                    swapped = True
            if not swapped:
                break
        return self.nums
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        middle = (left + right)
        if target == sorted_list[middle]:
            return middle
        elif target > sorted_list[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return left
def insert_into_sorted_list(n, sorted_list):
    if not sorted_list:
        sorted_list.append(n)
    else:
        index = binary_search(sorted_list, n)
        sorted_list.insert(index, n)
    return sorted_list
if __name__ == "__main__":
    sorter = MySorting([34, 10, -5, 72, 0, 8])
    print(sorter)
    print("Sorted in ascending order:", sorter.asc())
    print("Sorted in descending order:", sorter.desc())
    sorted_list = [10, 20, 30, 40]
    print("Inserting 25 into sorted list:", insert_into_sorted_list(25, sorted_list))