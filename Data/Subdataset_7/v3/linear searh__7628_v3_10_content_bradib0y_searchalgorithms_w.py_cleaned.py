import time
def fonk1(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
def fonk2(start, end):
    return range(start, end)
def fonk3():
    b1 = fonk2(0, 9999999)
    b2 = fonk2(100, 10000100)
    b3 = time.time()
    b4 = fonk1(b1, b2)
    b5 = time.time() - b3
    print("Time elapsed:", b5)
    print("Result list length:", len(b4))
    for item in b4:
        if item % b6 = = 0:
            print(item)
if b7 = = "__main__":
    fonk3()