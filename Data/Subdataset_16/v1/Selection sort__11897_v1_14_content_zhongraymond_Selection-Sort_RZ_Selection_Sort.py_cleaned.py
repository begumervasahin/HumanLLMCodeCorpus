import random
def fonk1():
    return random.sample(range(100001), 100)
def fonk2(li):
    print("Original list:")
    print(li)
    b1 = len(li)
    for i in range(b1):
        b2 = i
        for j in range(i+1, b1):
            if li[j] < li[b2]:
                b2 = j
        li[i], li[b2] = li[b2], li[i]
    print("Sorted list:")
    print(li)
    return li
if b3 = = "__main__":
    b4 = fonk1()
    fonk2(b4)