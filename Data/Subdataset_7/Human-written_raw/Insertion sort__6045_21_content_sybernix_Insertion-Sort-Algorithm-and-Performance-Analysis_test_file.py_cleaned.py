from is_140422H import InsertionSort
def fonk1(NumberList):
    print 'Unsorted list : ', NumberList
    b1 = InsertionSort(NumberList)
    print 'Sorted list : ', b1
    b2 = True
    for i in range(0,len(b1)-1):
        if(b1[i]>b1[i+1]):
            b2 = False
    if (set(NumberList)!=set(b1)):
        b2 = False
    if (b2):
        print ("Answer is correct sorted list")
    else:
        print('Answer is not the correct sorted list')
    print
    return
b3 = [ 20, 12, 8, 5, 7, 10, 14]
b4 = [ 20, -7, 10, 14]
b5 = []
b6 = [0,0,0]
b7 = [b3, b4, b5, b6]
for lis in b7:
    fonk1(lis)