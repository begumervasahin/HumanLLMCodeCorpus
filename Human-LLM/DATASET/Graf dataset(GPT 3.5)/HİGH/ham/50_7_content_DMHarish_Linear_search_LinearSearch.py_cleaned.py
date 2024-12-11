'''A Binary search is an algorithm which searches b3 b2 value in b3 list of
numbers. We use for loop to iterate through the list and then we print the
True or False if the algorithm finds that number and when it doesnot respectively'''
import random
b1 = [1,2,3,4,5,6]
def fonk1(b1,b2):
    for i in range(len(b1)):
        if b1[i] == b2:
            return True
        else:
            return False
b2 = random.randrange(1,10)
print(b1)
print(b2)
b3 = fonk1(b1,b2)
print(b3)