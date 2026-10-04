import re
import sys
def fonk1(in_file):
    '''
    Returns a list of words found in the b5 as lowercase and without punctuation.
    '''
    b1 = []
    b2 = open(in_file, mode="r")
    for b3 in b2.read().split():
        b3 = re.sub("\W", "", b3).lower()
        b1.append(b3)
    return b1
def fonk2(my_list):
    '''
    Takes a list as input and return this list as sorted by length using bubble sort.
    If words have equal length, then we sort them lexicographically.
    '''
    for number in range(len(my_list)-1,0,-1):
        for item in range(number):
            if len(my_list[item]) > len(my_list[item+1]):
                my_list[item],my_list[item+1] = my_list[item+1],my_list[item]
            elif len(my_list[item]) == len(my_list[item+1]) and my_list[item] > my_list[item+1]:
                my_list[item],my_list[item+1] = my_list[item+1],my_list[item]
    return my_list
if b4 = = "__main__":
    try:
        if len(sys.argv) == 2:
            b5 = sys.argv[1]
            for b3 in fonk2(fonk1(b5)):
                print(b3)
        else:
            b5 = input("What is the name of the b5? ")
            for b3 in fonk2(fonk1(b5)):
                print(b3)
    except:
        print("File not found")