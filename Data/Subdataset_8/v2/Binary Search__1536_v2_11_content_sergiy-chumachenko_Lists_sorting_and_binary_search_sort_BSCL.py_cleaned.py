class MySorting:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return "MySorting object containing: {}".format(self.nums)
    def asc(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
        return self.nums
    def desc(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.nums[j] < self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
        return self.nums
def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right)
        if lst[mid] < n:
            left = mid + 1
        elif lst[mid] > n:
            right = mid - 1
        else:
            return mid
    return left
def general_list(n, lst):
    index = binary_search(lst, n)
    lst.insert(index, n)
    return lst
nums = [5, 2, 9, 1, 7]
my_sorting = MySorting(nums)
print("Ascending:", my_sorting.asc())
print("Descending:", my_sorting.desc())
num_list = [1, 3, 5, 7, 9]
print("Updated list:", general_list(4, num_list))