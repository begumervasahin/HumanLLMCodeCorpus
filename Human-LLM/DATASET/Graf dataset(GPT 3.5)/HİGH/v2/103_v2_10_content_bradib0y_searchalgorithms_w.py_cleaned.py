import time
def fonk1(list1, list2):
    b1 = []
    for i in range(len(list1)):
        b1.append(list1[i] + list2[i])
    return b1
b2 = range(0, 9999999)
b3 = range(100, 10000100)
b4 = time.time()
b1 = fonk1(b2, b3)
b5 = time.time() - b4
print("Time elapsed:", b5)
print("Result list length:", len(b1))
for item in b1:
    if item % b6 = = 0:
        print(item)