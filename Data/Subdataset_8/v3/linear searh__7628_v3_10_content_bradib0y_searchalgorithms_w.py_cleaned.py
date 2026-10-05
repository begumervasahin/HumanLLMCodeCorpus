import time
def add_lists(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
def generate_consecutive_range(start, end):
    return range(start, end)
def main():
    nums1 = generate_consecutive_range(0, 9999999)
    nums2 = generate_consecutive_range(100, 10000100)
    start_time = time.time()
    result = add_lists(nums1, nums2)
    elapsed_time = time.time() - start_time
    print("Time elapsed:", elapsed_time)
    print("Result list length:", len(result))
    for item in result:
        if item % 777777 == 0:
            print(item)
if __name__ == "__main__":
    main()