import time
def add(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result
nums1 = range(0, 9999999)
nums2 = range(100, 10000100)
start_time = time.time()
result = add(nums1, nums2)
elapsed_time = time.time() - start_time
print("Time elapsed:", elapsed_time)
print("Result list length:", len(result))
for item in result:
    if item % 777777 == 0:
        print(item)