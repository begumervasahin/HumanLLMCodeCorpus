class MySorting:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return f"MySorting object containing: {self.nums}"
    def bubble_sort(self, reverse=False):
        n = len(self.nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if reverse:
                    if self.nums[j] < self.nums[j+1]:
                        self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                else:
                    if self.nums[j] > self.nums[j+1]:
                        self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
        return self.nums
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right)
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            return mid
    return left
def insert_sorted_list(lst, n):
    index = binary_search(lst, n)
    lst.insert(index, n)
    return lst
nums = [5, 2, 9, 1, 7]
my_sorting = MySorting(nums)
print("Ascending:", my_sorting.bubble_sort())
print("Descending:", my_sorting.bubble_sort(reverse=True))
num_list = [1, 3, 5, 7, 9]
print("Updated list:", insert_sorted_list(num_list, 4))