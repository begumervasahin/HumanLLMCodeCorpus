import random
import pickle
import time
import matplotlib.pyplot as plt
ar=random.sample(range(-100000,100000),100000)
global time_list_bubble_sort
time_list_bubble_sort=[]
global time_list_insertion_sort
time_list_insertion_sort=[]
global avg_time_bubble_sort
avg_time_bubble_sort=0.0
global avg_time_insertion_sort
avg_time_insertion_sort=0.0
def input(ar):
    avg_time_bubble_sort=[]
    avg_time_insertion_sort=[]
    input_list=[]
    ar=random.sample(range(1,300000),200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(ar,fp)
    with open("data.txt", 'rb') as fp:
        ar=pickle.load(fp)
    k=2000
    for i in range (0,25):
        time_list_bubble_sort=[]
        time_list_insertion_sort=[]
        sum_time_bubble_sort=0.0
        sum_time_insertion_sort=0.0
        for j in range(0,10):
            ar1=random.sample(ar,k)
            ar2=random.sample(ar,k)
            start_time_bubble_sort=time.time()
            bubble_sort(ar1)
            end_time_bubble_sort=time.time()
            total_time_bubble_sort=end_time_bubble_sort-start_time_bubble_sort
            time_list_bubble_sort.append(total_time_bubble_sort)
            sum_time_bubble_sort=sum_time_bubble_sort+time_list_bubble_sort[j]
            start_time_insertion_sort=time.time()
            insertion_sort(ar2)
            end_time_insertion_sort=time.time()
            total_time_insertion_sort=end_time_insertion_sort-start_time_insertion_sort
            time_list_insertion_sort.append(total_time_insertion_sort)
            sum_time_insertion_sort=sum_time_insertion_sort+time_list_insertion_sort[j]
        avg_time_bubble_sort.append(sum_time_bubble_sort/10)
        avg_time_insertion_sort.append(sum_time_insertion_sort/10)
        print(avg_time_bubble_sort)
        print(avg_time_insertion_sort)
        k=k+2000
    for i in range(1,26):
        input_list.append(2000*i)
    plt.plot(input_list,avg_time_bubble_sort,'r--' ,input_list,avg_time_insertion_sort,'b--')
    plt.show()
def bubble_sort(ar):
    global time_list
    global avg_time
    n=len(ar)
    for i in range (0,n):
        for j in range (0,n-1):
            if(ar[j]>ar[j+1]):
                temp = ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
def insertion_sort(ar):
    n=len(ar)
    for j in range (1,n):
        key=ar[j]
        i=j-1
        while(i>=0 and ar[i]>key):
            ar[i+1]=ar[i]
            i=i-1
        ar[i+1] = key
input(ar)