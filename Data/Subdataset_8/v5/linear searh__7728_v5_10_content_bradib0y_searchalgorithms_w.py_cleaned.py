import time
def add_lists(list1, list2):
    result = []
    for num1, num2 in zip(list1, list2):
        result.append(num1 + num2)
    return result
nums1 = range(0, 9999999)
nums2 = range(100, 10000100)
start_time = time.time()
result_list = add_lists(nums1, nums2)
elapsed_time = time.time() - start_time
print("Time elapsed:", elapsed_time)
print("Result list length:", len(result_list))
for item in result_list:
    if item % 777777 == 0:
        print(item)
