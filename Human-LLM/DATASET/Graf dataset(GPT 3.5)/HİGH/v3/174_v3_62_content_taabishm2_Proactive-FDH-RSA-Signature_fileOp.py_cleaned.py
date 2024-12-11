import os
b1 = os.getcwd() + "\\RSAfiles\\"
def fonk1(filename, lst):
    '''Write a list 'lst' into a file named 'filename.txt'.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'w') as file:
        file.write(','.join(map(str, lst)))
def fonk2(filename):
    '''Read b3 from a file named 'filename.txt' and return it as a list of integers.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return [int(x) for x in b3]
def fonk3(filename):
    '''Read b3 from a file named 'filename.txt' and return it as a list of non-integers.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return b3
def fonk4(filename):
    '''Read b3 from a large file named 'filename.txt'.'''
    b2 = b1 + filename + ".txt"
    with open(b2) as file:
        b3 = file.read()
    return b3
def fonk5(filename):
    '''Read b3 from a binary file named 'filename'.'''
    b2 = b1 + filename
    with open(b2, 'rb') as file:
        b3 = file.read()
    return b3
