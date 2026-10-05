def fonk1(lst, target):
    for b1 in lst:
        if b1 = = target:
            return True
    return False
b2 = [10, 20, 30, 40, 50]
a1 = 30
print(fonk1(b2, a1))
def fonk2(lst, target):
    if not lst:
        return False
    b3 = len(lst)
    if lst[b3] == target:
        return True
    elif target < lst[b3]:
        return fonk2(lst[:b3], target)
    else:
        return fonk2(lst[b3 + 1:], target)
b4 = [10, 20, 30, 50, 60, 70, 80]
a1 = 50
print(fonk2(b4, a1))