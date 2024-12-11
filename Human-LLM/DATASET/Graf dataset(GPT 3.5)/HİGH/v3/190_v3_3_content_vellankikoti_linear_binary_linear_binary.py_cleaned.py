def fonk1(lst, key):
    return key in lst
b1 = [10, 20, 30, 40, 50]
a1 = 30
print(f"Linear Search: {fonk1(b1, a1)}")
def fonk2(lst, key):
    if not lst:
        return False
    b2 = len(lst)
    if lst[b2] == key:
        return True
    elif key < lst[b2]:
        return fonk2(lst[:b2], key)
    else:
        return fonk2(lst[b2 + 1:], key)
b3 = [10, 20, 30, 50, 60, 70, 80]
a2 = 50
print(f"Binary Search: {fonk2(b3, a2)}")