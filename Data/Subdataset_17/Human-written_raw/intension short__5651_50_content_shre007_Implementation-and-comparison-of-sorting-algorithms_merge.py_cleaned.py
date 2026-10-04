def mergesort(givenlist):
    if len(givenlist) > 1:
        mid = len(givenlist)
        left_list = givenlist[:mid]
        right_list = givenlist[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0
        while len(left_list) > i and len(right_list) > j:
            if left_list[i] < right_list[j]:
                givenlist[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                givenlist[k] = right_list[j]
                j = j + 1
                k = k + 1
        while len(left_list)>i :
            givenlist[k] = left_list[i]
            i = i + 1
            k = k + 1
        while len(right_list)>j :
            givenlist[k] = right_list[j]
            j = j + 1
            k = k + 1
number = int(input("how many elements you want in this list: "))
givenlist = [int(input()) for x in range(number)]
mergesort(givenlist)
print("sorted list is: ", givenlist)