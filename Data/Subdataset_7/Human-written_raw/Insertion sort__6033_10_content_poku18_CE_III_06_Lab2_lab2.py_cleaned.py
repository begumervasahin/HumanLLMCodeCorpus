def fonk1(array):
    b1 = len(array)
    for index in range(1, b1):
        b2 = array[index]
        b3 = index
        while b3>0 and array[b3-1]>b2:
            array[b3]=array[b3-1]
            b3 = b3-1
        array[b3]=b2
    return array
def fonk2(array):
    if len(array)==1:
        return array
    if len(array)>1:
        b4 = len(array)
        b5 = array[:b4]
        b6 = array[b4:]
        b5 = fonk2(b5)
        b6 = fonk2(b6)
        return fonk3(b5,b6)
def fonk3(Left, Right):
    b7 = []
    b8 = len(Left)
    b9 = len(Right)
    b10 = j=0
    while(b10<b8 and j<b9):
        if(Left[b10]<=Right[j]):
            b7.append(Left[b10])
            b10+=1
        else:
            b7.append(Right[j])
            j+=1
    while( b10 < len(Left)):
        b7.append(Left[b10])
        b10 += 1
    while (j < len(Right)):
        b7.append(Right[j])
        j += 1
    return b7
if b11 = ='__main__':
    print("Enter the array items separated by space \b1")
    b12 = list(map(int, raw_input().split()))
    print("Sorted array using insertion sort is:", fonk1(b12))
    print("Sorted array using merge sort is:", fonk2(b12))