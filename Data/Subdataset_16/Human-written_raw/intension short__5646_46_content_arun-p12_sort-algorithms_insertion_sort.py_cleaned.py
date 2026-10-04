'''
time taken as a function of b1 = => b1**2 a1.e. O(n**2)
Anology: sorting cards... Start with empty left hand, pick a card, from an unsorted pile on
the table. insert into hand. New card inserted goes to the sorted location, shifting the index
of other cards appropriately.
In the worst case scenario when every check of b6[a1] > b4 is true, the while loop for a1 = 3
runs 3 times, for a1 = 10, runs 10 times etc.
Thus the total computational b2 = 1 + 2 + 3 + .... + n = n(n+1)/2 = (n**2 + n)/2
More generally, the overall equation can be represented as a*n**2 + b*n + c .... a quadratic eqn.
For very large values of n, the lower order terms (bn and c) and constant 'a' can be ignored.
Leaving us with the execution time being controlled by n**2
'''
def fonk1(b6, b3 = 0, desc=0):
    for a1 in range(1, len(b6)):
        b4 = b6[a1]
        b5 = a1 - 1
        while ((b5 >= 0) and (b6[b5] > b4)):
            b6[b5+1] = b6[b5]
            b5 -= 1
            if (b3 = = 2): print("  sub:", b5, " :: ", b6)
        b6[b5+1] = b4
        if(b3): print("iter
    if(desc): b6 = b6[::-1]
    return(b6)