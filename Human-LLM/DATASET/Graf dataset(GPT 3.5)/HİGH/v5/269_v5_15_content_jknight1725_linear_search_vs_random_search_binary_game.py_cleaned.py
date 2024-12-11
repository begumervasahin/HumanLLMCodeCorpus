from myFunctions import *
a1 = 1
lower_bound, b1 = 0, 1000
b2 = mid(lower_bound, b1)
computer_says(b2)
while True:
    b3 = get_adjustment()
    if b3 = = 'c':
        break
    lower_bound, b1 = make_adjustment(b3, b2, lower_bound, b1)
    b2 = mid(lower_bound, b1)
    a1 += 1
    computer_says(b2)
found(b2, a1)