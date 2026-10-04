def insertionSort(array):
    n=len(array)
    for index in range(1, n):
        current= array[index]
        position= index
        while position>0 and array[position-1]>current:
            array[position]=array[position-1]
            position = position-1
        array[position]=current
    return array
def mergeSort(array):
    if len(array)==1:
        return array
    if len(array)>1:
        mid=len(array)
        left=array[:mid]
        right=array[mid:]
        left =mergeSort(left)
        right=mergeSort(right)
        return merge(left,right)
def merge(Left, Right):
    result=[]
    n1=len(Left)
    n2=len(Right)
    i=j=0
    while(i<n1 and j<n2):
        if(Left[i]<=Right[j]):
            result.append(Left[i])
            i+=1
        else:
            result.append(Right[j])
            j+=1
    while( i < len(Left)):
        result.append(Left[i])
        i += 1
    while (j < len(Right)):
        result.append(Right[j])
        j += 1
    return result
if __name__=='__main__':
    print("Enter the array items separated by space \n")
    inparray = list(map(int, raw_input().split()))
    print("Sorted array using insertion sort is:", insertionSort(inparray))
    print("Sorted array using merge sort is:", mergeSort(inparray))