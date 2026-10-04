def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchanges = True
        passnum -= 1
test_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(test_list)
print(test_list)
