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
                i += 1
            else:
                givenlist[k] = right_list[j]
                j += 1
            k += 1
        while len(left_list) > i:
            givenlist[k] = left_list[i]
            i += 1
            k += 1
        while len(right_list) > j:
            givenlist[k] = right_list[j]
            j += 1
            k += 1
number = int(input("How many elements do you want in this list: "))
givenlist = [int(input("Enter element: ")) for _ in range(number)]
mergesort(givenlist)
print("Sorted list:", givenlist)