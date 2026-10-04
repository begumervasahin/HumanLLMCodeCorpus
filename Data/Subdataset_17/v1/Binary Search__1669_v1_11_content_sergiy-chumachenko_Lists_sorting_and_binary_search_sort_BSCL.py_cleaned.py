class MySorting:
    def __init__(self, nums):
        self.nums = nums
    def __str__(self):
        return f"MySorting method can be used to sort your list:\n{self.nums}"
    def asc(self):
        n = len(self.nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    swapped = True
            if not swapped:
                break
        return self.nums
    def desc(self):
        n = len(self.nums)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.nums[j] < self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    swapped = True
            if not swapped:
                break
        return self.nums
def binary_search(lst, n):
    left, right = 0, len(lst) - 1
    while left <= right:
        middle = (left + right)
        if lst[middle] < n:
            left = middle + 1
        elif lst[middle] > n:
            right = middle - 1
        else:
            return middle
    return left
def general_list(n, lst):
    if not lst:
        lst.append(n)
    else:
        index = binary_search(lst, n)
        lst.insert(index, n)
    return lst
if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorter = MySorting(nums)
    print("Original list:", nums)
    print("Sorted list (ascending):", sorter.asc())
    print("Sorted list (descending):", sorter.desc())
    sorted_list = [1, 3, 5, 7, 9]
    new_number = 6
    print(f"Inserting {new_number} into {sorted_list}:")
    updated_list = general_list(new_number, sorted_list)
    print("Updated list:", updated_list)