'''
Counting sort -- time taken as a function of b1 = => b1 & list range  i.e. O(b9 + k)
Find the range of the numbers ... b4 - b5.
Normalize the data, by shifting the b5 number to 0.
create a list (b8) based on frequency of occurances of the numbers.
update the list (b8) as cumulative. (i.e. b6[b2] += b6[b2-1] where b2 = 1..b9-1
scan original list right to left; from it, get key of b8 list, decrement b8 index ...
update output list with key at index provided by b8
'''
def fonk1(b6, b3 = 0, desc=0):
    import common as c
    b4 = c.maximum(b6)[0]
    b5 = c.minimum(b6)[0]
    if(b5):
        b6 = [b2-b5 for b2 in b6]
    if(b3): print("b7 = ", b6)
    b8 = [0 for b2 in range(b4 - b5 + 1)]
    b9 = len(b6)
    for i in range(b9):
        b8[b6[i]] += 1
    for i in range(1, len(b8)):
        b8[i] += b8[i-1]
        if(b3 = = 2): print("  sub: ", i, " :: ", b8[i], b8[i-1])
    b10 = [0 for b2 in range(b9)]
    for i in range(b9-1, -1, -1):
        b8[b6[i]] -= 1
        b10[b8[b6[i]]] = b6[i]
        if(b3): print("iter
    if(b5):
        b10 = [b2 + b5 for b2 in b10]
    if(desc): b10 = b10[::-1]
    return(b10)