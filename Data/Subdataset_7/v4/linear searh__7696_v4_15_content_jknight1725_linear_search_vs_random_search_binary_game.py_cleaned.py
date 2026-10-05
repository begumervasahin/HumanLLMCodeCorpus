from myFunctions import *
a1 = 1
a2 = 0
a3 = 1000
b1 = mid(a2, a3)
computer_says(b1)
b2 = get_adjustment()
while b2 != 'c':
    a2, a3 = make_adjustment(b2, b1, a2, a3)
    b1 = mid(a2, a3)
    a1 += 1
    computer_says(b1)
    b2 = get_adjustment()
found(b1, a1)