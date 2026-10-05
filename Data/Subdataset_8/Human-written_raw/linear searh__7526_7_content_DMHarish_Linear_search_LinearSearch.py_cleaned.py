'''A Binary search is an algorithm which searches a target value in a list of
numbers. We use for loop to iterate through the list and then we print the
True or False if the algorithm finds that number and when it doesnot respectively'''
import random
data = [1,2,3,4,5,6]
def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True
        else:
            return False
target=random.randrange(1,10)
print(data)
print(target)
a=linear_search(data,target)
print(a)