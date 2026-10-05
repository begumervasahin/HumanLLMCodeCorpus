'''
->The main purpose of this program is to test the different sorting algorithms. They are tested by determining the time taken for
      each algorithm to sort the given array, the number of array accesses made and the use of extra memory by creating more arrays.
->We DO NOT use lists in this lab. We use ctype arrays to implement the algorithms.
->This program prompts the user to choose the sorting algorithm from the menu they want to use to sort the numbers.
->The user is also prompted to enter the number upto which the values will be sorted. Eg: If the user inputs n,
      then we will have values from 1...n in the array to be sorted.
'''
import ctypes
import random
import time
class SelectionSort:
        def __init__(this, array):
                this.array = array
                this.array_accesses = 0
                this.extra_memory = 0
                this.recursive_calls = 0
                this.selectionsort()
        def selectionsort(this):
                for i in range(len(this.array)-1,0,-1):
                        max_position = 0
                        for location in range(1,i+1):
                                this.array_accesses += 2
                                if this.array[location] > this.array[max_position]:
                                        max_position  = location
                        temp = this.array[i]
                        this.array[i] = this.array[max_position]
                        this.array[max_position] = temp
                        this.array_accesses += 4
                return this.array
class QuickSort():
        def __init__(this,array, start, end):
                this.array = array
                this.extra_memory = 0
                this.array_accesses = 0
                this.recursive_calls = -1
                this.quick_sort(array,start, end)
        def quick_sort(this, array, start, end):
                this.recursive_calls += 1
                if start < end:
                        pivot = this.partition(array,start,end)
                        this.quick_sort(array ,start   ,pivot-1)
                        this.quick_sort(array ,pivot+1 ,end    )
        def partition(this, array, first, last):
                big = first + 1
                small = last
                pivot = array[first] ; this.array_accesses += 1
                while (big <= small) :
                        while (big <= last and array[big] <= pivot) :
                                this.array_accesses += 1
                                big += 1
                        while array[small] > pivot :
                                this.array_accesses += 1
                                small -= 1
                        if big < small :
                                temp1 = array[small]
                                array[small] = array[big]
                                array[big] = temp1
                                this.array_accesses += 4
                temp2 = array[first]
                array[first] = array[small]
                array[small] = temp2
                this.array_accesses += 4
                return small
class MergeSort():
        def __init__(this, array, array_accesses=0):
                this.array = array
                this.extra_memory = 0
                this.array_accesses = 0
                this.recursive_calls = -1
                this.array = MergeSort.mergesort(this, array)
        def mergesort(this, array):
                this.recursive_calls += 1
                n = len(array)
                if n <= 1:
                        return array
                left_array = (n
                this.extra_memory += n
                for index in range(n
                        left_array[index] = array[index]
                        this.array_accesses += 2
                this.extra_memory += n-(n
                right_array = ((n-(n
                for index in range(n
                        right_array[index-(n
                        this.array_accesses += 2
                list1 = MergeSort.mergesort(this, left_array)
                list2 = MergeSort.mergesort(this, right_array)
                array = MergeSort.merge(this, list1, list2)
                return array
        def merge(this, l1,l2):
                this.extra_memory += len(l1)+len(l2)
                final_array = ((len(l1)+len(l2) ) * ctypes.py_object)()
                ind=0
                i=0
                j=0
                while i<len(l1)  and j<len(l2):
                        this.array_accesses += 2
                        if l1[i] < l2[j]:
                                final_array[ind]=l1[i]
                                this.array_accesses += 2
                                i+=1
                                ind+=1
                        else:
                                final_array[ind]=l2[j]
                                this.array_accesses += 2
                                j+=1
                                ind+=1
                while( i < len(l1)):
                        final_array[ind]=l1[i]
                        this.array_accesses += 2
                        i+=1
                        ind+=1
                while (j < len(l2)):
                        final_array[ind]=l2[j]
                        this.array_accesses += 2
                        j+=1
                        ind+=1
                return final_array
class HeapSort:
        def __init__(this, array):
                this.array = array
                this.extra_memory = 0
                this.recursive_calls = 0
                this.array_accesses = 0
                this._size=len(this.array)
                i=(this._size-2)
                while i>=0:
                        this.max_heap(i)
                        i-=1
                this.heapSort()
        def max_heap(this,index):
                largest=index
                left=2*index+1
                right=2*index+2
                this.array_accesses += 2
                if left < this._size and this.array[left] > this.array[largest]:
                        largest=left
                this.array_accesses += 2
                if right < this._size and this.array[right] >this.array[largest]:
                        largest=right
                if not largest==index:
                        temp = this.array[largest]
                        this.array[largest] = this.array[index]
                        this.array[index] = temp
                        this.array_accesses += 4
                        this.recursive_calls += 1
                        this.max_heap(largest)
        def heapSort(this):
                while this._size >1:
                        temp = this.array[0]
                        this.array[0] = this.array[this._size-1]
                        this.array[this._size-1] = temp
                        this.array_accesses += 4
                        this._size-=1
                        this.max_heap(0)
                return this.array
def create_array(given_array_size):
        numbers_in_array = (given_array_size * ctypes.py_object)()
        for value in range(1, given_array_size+1):
                numbers_in_array[value-1] = value
        return numbers_in_array
def shuffle_array(array):
        for element in range(len(array)-1,0,-1):
                random_index = random.randint(0, element)
                temp = array[element]
                array[element] = array[random_index]
                array[random_index] = temp
        return array
def main():
        while True:
                print("1: Merge Sort\n"
                      "2: Heap Sort\n"
                      "3: Quick Sort\n"
                      "4: Selection Sort\n"
                      "5: Exit\n")
                try:
                        user_input = int(input("Enter your choice:\t"))
                        if user_input < 1 or user_input > 5:
                                print("\nInvalid input. Try Again!\n\n")
                                continue
                        array_size = int(input("Enter the number of elements in the Array:\t"))
                except:
                        print("\nInvalid input. Try again!\n\n")
                        continue
                unsorted_array = create_array(array_size)
                shuffle_array(unsorted_array)
                print("Array Before Sorting:")
                for i in range(0, array_size):
                        print(unsorted_array[i], end = ", " if i != array_size-1 else "\n\n")
                starting_time = time.time()
                if user_input == 1:
                        print("***Merge Sort***")
                        recursive_calls = 0
                        sorted_array = MergeSort(unsorted_array, 0)
                elif user_input == 2:
                        print("***Heap Sort***")
                        sorted_array = HeapSort(unsorted_array)
                elif user_input == 3:
                        print("***Quick Sort***")
                        sorted_array = QuickSort(unsorted_array,0,len(unsorted_array)-1)
                elif user_input == 4:
                        sorted_array = SelectionSort(unsorted_array)
                elif user_input == 5:
                        print("\nExiting program...\n")
                        exit()
                elapsed_time = time.time() - starting_time
                print("Array After Sorting:")
                for i in range(0, array_size):
                        print(sorted_array.array[i], end = ", " if i != array_size-1 else "\n\n")
                print("Elapsed Time:\t\t\t\t\t\t\t", elapsed_time, "seconds")
                print("Numbers of array accesses:\t\t\t\t\t"+str(sorted_array.array_accesses))
                print("Number of extra memory space occupied:\t\t"+str(sorted_array.extra_memory))
                print("Number of recursive calls:\t\t\t\t\t"+str(sorted_array.recursive_calls),end="\n\n\n")
main()