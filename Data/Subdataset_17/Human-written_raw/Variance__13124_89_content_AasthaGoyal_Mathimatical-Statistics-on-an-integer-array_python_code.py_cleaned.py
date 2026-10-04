import os
import sys
import math
stat=[]
temp_list =[]
sort_list=[]
error_list=[]
condition = True
while(condition == True):
    phrase = input("Enter a list of numbers:")
    temp_list = phrase.split(",")
    stat.extend(temp_list)
    for item in stat:
        if(item.isdigit()==False):
            print(item, "is not an integer value")
            error_list.append(item)
            if (item == "Terminate"):
                stat.remove(item)
                print("You terminated the program")
                condition = False
            else:
                 stat.remove(item)
while stat:
    min_value = stat[0]
    for x in stat:
        if x < min_value:
            min_value = x
    sort_list.append(min_value)
    stat.remove(min_value)
print (sort_list)
for i in range(0,len(sort_list)):
    sort_list[i] = int(sort_list[i])
maximum = sort_list[-1]
minimum = sort_list[0]
range_value = maximum - minimum
total_count = len(sort_list)
sum1 =0
for i in range (0,len(sort_list)):
    sum1 = sum1 + sort_list[i]
    i=i+1
mean = sum1/total_count
count =1
i=0
print("1) The number of each individual number:")
for i in range (0,len(sort_list)):
    count = 0
    for j in range(1,len(sort_list)):
        if(sort_list[i]== sort_list[j]):
            count = count+1
    print(sort_list[i], ":", count)
for i in range(0,len(sort_list)):
    d = (sort_list[i]- mean)**2
    variance = d/total_count
std = math.sqrt(variance)
print("2) The Maximum value is:", maximum)
print("3) The Minimum value is:", minimum)
print("4) The Range of the two numbers is:", range_value)
print("5) Arithmetic Mean of the two numbers is:", mean)
print("6) Variance of the two numbers si:", variance)
print("7) The Standard Deviation of two numbers is:",std)
print("8)", error_list)