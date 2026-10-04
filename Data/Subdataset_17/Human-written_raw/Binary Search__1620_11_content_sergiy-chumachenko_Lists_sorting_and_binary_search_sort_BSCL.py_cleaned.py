class My_sorting(object):
    def __init__(self,nums):
        self.nums = nums
    def __str__(self):
        return ("My_sorting method can be used to sort your list:\n{}".format(self.nums))
    def asc(self):
        replace = 0
        n = 1
        while n<len(self.nums):
            for i in range(len(self.nums)-n):
                if self.nums[i]>self.nums[i+1]:
                    self.nums[i],self.nums[i+1] = self.nums[i+1],self.nums[i]
                    replace +=1
            if replace == 0:
                break
            else:
                n+=1
        return self.nums
    def desc(self):
        replace = 0
        n = 1
        while n<len(self.nums):
            for i in range(len(self.nums)-n):
                if self.nums[i]<self.nums[i+1]:
                    self.nums[i],self.nums[i+1] = self.nums[i+1],self.nums[i]
                    replace +=1
            if replace == 0:
                break
            else:
                n+=1
        return self.nums
def binary(list,n):
    left = 0
    right = len(list)-1
    middle = round(right/2)
    while left<middle and middle < right:
        if n > list[middle] and middle < right:
            left = middle
        elif n < list[middle] and left < middle:
            right = middle
        elif n == list[middle]:
            return middle
        middle = round((left+right)/2)
        if left >= right:
            return left
        elif middle >= right:
            return right
        elif left >= middle:
            return left +1
        else:
            continue
def general_list(n,list):
    i = len(list)
    if i == 0:
        list.append(n)
    elif i == 1:
        if n >= list[0]:
            list.append(n)
        elif n <list[0]:
            list.insert(0,n)
    elif i == 2:
        if n >= list[-1]:
            list.append(n)
        elif n <= list[0]:
            list.insert(0,n)
        else:
            list.insert(1,n)
    elif i > 2:
        if n <= list[0]:
            list.insert(0,n)
        elif n >= list[-1]:
            list.append(n)
        elif list[0]<n<list[-1]:
            indx = binary(list,n)
            list.insert(indx,n)
    return list