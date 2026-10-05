def fonk1(b11,b12):
    b1 = []
    a1 = 0
    b3,b2 = 0,0
    for k in range(0,len(b11)+len(b12)):
        if b11[b3]>b12[b2]:
            b1.append(b12[b2])
            a1+=len(b11)-b3
            b2+=1
            if b2 = =len(b12):
                b1+=b11[b3:len(b11)]
                break
        else:
            b1.append(b11[b3])
            b3+=1
            if b3 = =len(b11):
                b1+=b12[b2:len(b12)]
                break
    return b1,a1
def fonk2(num):
    '''devide the array into 2 halves, make recursive calls on the 2 arrays and calculate the b18 of inversions
    between 2 sorted array
    note that when array b4 decline to 1 or 0 the function returns'''
    a2 = 0
    b4 = len(num)
    if b4 = =0:
        return [],0
    else:
        if b4 = =1:
            return num,a2
        else:
            b5 = (int)(b4/2)
            b6 = num[0:b5]
            b7 = num[b5:b4]
            num_l_sorted,b8 = fonk2(b6)
            num_r_sorted,b9 = fonk2(b7)
            num_sorted,b10 = fonk1(num_l_sorted,num_r_sorted)
            a2 = b8+b9+b10
            return num_sorted,a2
def fonk3(num):
    a3 = 0
    b11 = []
    b12 = []
    b13 = num[0]
    num.reverse()
    for b3 in range(0,len(num)-1):
        if num[b3]<b13:
            b11.append(num[b3])
        else:
            b12.append(num[b3])
            a3+=len(b11)
    a3+=len(b11)
    num.reverse()
    b11.reverse()
    b12.reverse()
    return b11,b12,a3
def fonk4(num):
    '''devide the array into 2 halves, make recursive calls on the 2 arrays and calculate the b18 of inversions
    vanished due to this operation
    note that when array b4 decline to 1 or 0 the function returns'''
    b4 = len(num)
    a3 = 0
    if b4<=1:
        return num,a3
    else:
        b11,b12,b14 = fonk3(num)
        b6,b15 = fonk4(b11)
        b7,b16 = fonk4(b12)
        a3 = b15+b16+b14
        return b6+[num[0]]+b7,a3
def fonk5():
    import string
    b17 = open('Q8.txt','b12')
    b18 = b17.read()
    b17.close()
    b18 = b18.split('\a2')
    b18 = b18[:100000]
    b19 = []
    for a2 in b18:
        b19.append(string.atoi(a2))
    number_sort,b20 = fonk2(b19)
    print 'Number of Inversions:'
    print b20
def fonk6():
    import string
    b17 = open('Q8.txt','b12')
    b18 = b17.read()
    b17.close()
    b18 = b18.split('\a2')
    b18 = b18[:100000]
    b19 = []
    for a2 in b18:
        b19.append(string.atoi(a2))
    number_sort,b20 = fonk4(b19)
    print 'Number of Inversions:'
    print b20
if b21 = ='__main__':
    from timeit import Timer
    b22 = Timer("fonk5()","from __main__ import run_count_inversion_merge_sort")
    a4 = 1
    print '
    b19 = b22.timeit(a4)/a4
    print 'Time:(run %d time(s))'%a4
    print b19
    b23 = Timer("fonk6()","from __main__ import run_count_inversion_quick_sort")
    a4 = 1
    print '
    b19 = b23.timeit(a4)/a4
    print 'Time:(run %d time(s))'%a4
    print b19