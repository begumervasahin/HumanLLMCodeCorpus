def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        print(f"Step {i + 1}: {nums}")
        if not swapped:
            break
if __name__ == "__main__":
    nums = [5, 3, 8, 6, 7, 2]
    print("Unsorted List =", nums)
    bubble_sort(nums)
    print("Sorted List =", nums)