class MySorting(object):
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return "MySorting method can be used to sort your list:\n{}".format(self.nums)
    def asc(self):
        replace = 0
        n = 1
        while n < len(self.nums):
            for i in range(len(self.nums) - n):
                if self.nums[i] > self.nums[i + 1]:
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
                    replace += 1
            if replace == 0:
                break
            else:
                n += 1
        return self.nums
    def desc(self):
        replace = 0
        n = 1
        while n < len(self.nums):
            for i in range(len(self.nums) - n):
                if self.nums[i] < self.nums[i + 1]:
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
                    replace += 1
            if replace == 0:
                break
            else:
                n += 1
        return self.nums
def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    middle = round(right / 2)
    while left < middle and middle < right:
        if n > lst[middle] and middle < right:
            left = middle
        elif n < lst[middle] and left < middle:
            right = middle
        elif n == lst[middle]:
            return middle
        middle = round((left + right) / 2)
        if left >= right:
            return left
        elif middle >= right:
            return right
        elif left >= middle:
            return left + 1
        else:
            continue
def general_list(n, lst):
    i = len(lst)
    if i == 0:
        lst.append(n)
    elif i == 1:
        if n >= lst[0]:
            lst.append(n)
        elif n < lst[0]:
            lst.insert(0, n)
    elif i == 2:
        if n >= lst[-1]:
            lst.append(n)
        elif n <= lst[0]:
            lst.insert(0, n)
        else:
            lst.insert(1, n)
    elif i > 2:
        if n <= lst[0]:
            lst.insert(0, n)
        elif n >= lst[-1]:
            lst.append(n)
        elif lst[0] < n < lst[-1]:
            indx = binary_search(lst, n)
            lst.insert(indx, n)
    return lst
nums = [5, 2, 9, 1, 7]
my_sorting = MySorting(nums)
print(my_sorting.asc())
print(my_sorting.desc())
num_list = [1, 3, 5, 7, 9]
print(general_list(4, num_list))