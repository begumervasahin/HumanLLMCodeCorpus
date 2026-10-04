def SelectionSort(s):
    n=len(s)
    minindex=0
    for i in range(0,n):
        minindex=i
        for j in range(i+1,n):
            if(s[minindex]>s[j]):
                minindex=j
        if(i!=minindex):
            a=s[i]
            s[i]=s[minindex]
            s[minindex]=a
    return s
s=[6,3,1,9,2,5,8,7,4]
print SelectionSort(s)