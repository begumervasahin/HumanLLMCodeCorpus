class MySorting:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return f"MySorting object can be used to sort a list:\n{self.nums}"
    def bubble_sort(self, reverse=False):
        replace = 0
        n = 1
        while n < len(self.nums):
            for i in range(len(self.nums) - n):
                if (reverse and self.nums[i] < self.nums[i + 1]) or (not reverse and self.nums[i] > self.nums[i + 1]):
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
                    replace += 1
            if replace == 0:
                break
            else:
                n += 1
        return self.nums
    def insertion_sort(self, reverse=False):
        for i in range(1, len(self.nums)):
            current = self.nums[i]
            j = i - 1
            while j >= 0 and ((reverse and self.nums[j] < current) or (not reverse and self.nums[j] > current)):
                self.nums[j + 1] = self.nums[j]
                j -= 1
            self.nums[j + 1] = current
        return self.nums
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right)
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
def insert_into_list(n, lst):
    if not lst:
        lst.append(n)
    else:
        idx = binary_search(lst, n)
        lst.insert(idx, n)
    return lst