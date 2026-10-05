def bubble_sort(nums):
    '''
    Sorts a list of numbers using the Bubble Sort algorithm.
    '''
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
def main():
    nums = [5, 3, 8, 6, 7, 2]
    print("Unsorted List =", nums)
    bubble_sort(nums)
    print("Sorted List =", nums)
if __name__ == "__main__":
    main()