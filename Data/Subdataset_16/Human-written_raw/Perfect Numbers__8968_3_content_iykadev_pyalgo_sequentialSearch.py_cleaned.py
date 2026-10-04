def fonk1(alist, item):
	    a1 = 0
	    b1 = False
	    while a1 < len(alist) and not b1:
	        if alist[a1] == item:
	            b1 = True
	        else:
	            a1 = a1+1
	    return b1
b2 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(fonk1(b2, 3))
print(fonk1(b2, 13))