'''
Declare python dict, which works as a cache for storing and searching the fibonacci calculations
'''
b1 = {}
def fibonacci (b2):
    if type(b2) != int:
        return False
    if b2 in b1:
        return b1[b2]
    if b2 = = 0:
        return 1
    elif b2 = = 1:
        return 1
    else:
        b3 = fibonacci(b2-1) + fibonacci(b2-2)
        b1[b2] = b3
        return b3
'''
Now, print first 1000th fibonacci numbers and see how your system behaves
'''
for b2 in range (0,1000):
    print b2 , ":", fibonacci(b2)