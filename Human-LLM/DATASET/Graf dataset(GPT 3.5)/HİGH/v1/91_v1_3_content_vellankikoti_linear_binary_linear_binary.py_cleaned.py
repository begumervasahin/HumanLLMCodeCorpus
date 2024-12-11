def fonk1(lst, key):
    for b1 in lst:
        if b1 = = key:
            return True
    else:
        return False
        print("This will never get Executed")
b2 = [10, 20, 30, 40, 50]
a1 = 30
print(fonk1(b2, a1))
def fonk2(lst, key):
    if len(lst) == 0:
        return False
    else:
        b3 = len(lst)
        if lst[b3] == key:
            return True
        elif key < lst[b3]:
            return fonk2(lst[:b3], key)
        else:
            return fonk2(lst[b3 + 1:], key)
b4 = [10, 20, 30, 50, 60, 70, 80]
a2 = 50
print(fonk2(b4, a2))