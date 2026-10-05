import time
def add(list1, list2):
    result = []
    for i in range(0, len(list1)):
        result.append(list1[i] + list2[i])
    return result
nums1 = range(0, 9999999)
nums2 = range(100, 10000100)
ts = time.time()
r = add(nums1, nums2)
te = time.time() - ts
print("Time elapsed: ", te)
print("Result list length: ", len(r))
for item in r:
    if item % 777777 == 0:
        print(item)