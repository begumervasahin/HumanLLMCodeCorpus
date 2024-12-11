import time
def fonk1(list1, list2):
    b1 = []
    for i in range(0, len(list1)):
        b1.append(list1[i] + list2[i])
    return b1
b2 = range(0, 9999999)
b3 = range(100, 10000100)
b4 = time.time()
b5 = fonk1(b2, b3)
b6 = time.time() - b4
print("Time elapsed:", b6)
print("Result list length:", len(b5))
for item in b5:
    if item % b7 = = 0:
        print(item)
