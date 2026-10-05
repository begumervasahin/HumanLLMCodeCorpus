import time
import random
def selection_sort(arr):
    for k in range (0, len(arr)-1):
        min=k
        n=k+1
        while (n < len(arr)):
            if arr[n] < arr[min]:
                min = n
            n+=1
        temp = arr[min]
        arr[min] = arr[k]
        arr[k] = temp
    return arr
def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur
    return arr
if __name__ == '__main__':
    minVal = 0
    maxVal = 100
    start = 0.0
    end = 0.0
    averageTimes = [0] * 6
    length = int(input('How many values should be generated? '))
    arr_sel_inc = [0] * length
    arr_sel_dec = [0] * length
    arr_sel_ran = [0] * length
    arr_ins_inc = [0] * length
    arr_ins_dec = [0] * length
    arr_ins_ran = [0] * length
    tempArray = [0] * length
    times_sel_inc = [0] * 5
    times_sel_dec = [0] * 5
    times_sel_ran = [0] * 5
    times_ins_inc = [0] * 5
    times_ins_dec = [0] * 5
    times_ins_ran = [0] * 5
    tempTimes = [0] * 5
    for x in range(0,length):
        arr_sel_inc[x] = x + 1
    arr_ins_inc = arr_sel_inc
    for x in range(0,length):
        arr_sel_dec[x] = length - x
    arr_ins_dec = arr_sel_dec
    for x in range(0, length):
        arr_sel_ran[x] = random.randint(minVal, maxVal)
    arr_ins_ran = arr_sel_ran
    array_Arrays = [arr_sel_inc, arr_sel_dec, arr_sel_ran, \
    arr_ins_inc, arr_ins_dec, arr_ins_ran]
    array_Times = [times_sel_inc, times_sel_dec, times_sel_ran, \
    times_ins_inc, times_ins_dec, times_ins_ran]
    for index in range(0, 3):
        for count in range(0,5):
            tempArray = array_Arrays[index][:]
            start = time.clock()
            selection_sort(tempArray)
            end = time.clock()
            tempTimes[count] = end - start
        array_Times[index] = tempTimes[:]
    for index in range(3, 6):
        for count in range(0,5):
            tempArray = array_Arrays[index][:]
            start = time.clock()
            insertion_sort(tempArray)
            end = time.clock()
            tempTimes[count] = end - start
        array_Times[index] = tempTimes[:]
    for index in range(0,6):
        tempVal = 0
        tempTimes = array_Times[index][:]
        for count in range(0,5):
            tempVal = tempVal + tempTimes[count]
        averageTimes[index] = tempVal / 5
    print(str(length) + '-Val Increasing Selection: ' + '{:.20f}'.format(averageTimes[0]))
    print(str(length) + '-Val Decreasing Selection: ' + '{:.20f}'.format(averageTimes[1]))
    print(str(length) + '-Val Random Selection:     ' + '{:.20f}'.format(averageTimes[2]))
    print(str(length) + '-Val Increasing Insertion: ' + '{:.20f}'.format(averageTimes[3]))
    print(str(length) + '-Val Decreasing Insertion: ' + '{:.20f}'.format(averageTimes[4]))
    print(str(length) + '-Val Random Insertion:     ' + '{:.20f}'.format(averageTimes[5]))