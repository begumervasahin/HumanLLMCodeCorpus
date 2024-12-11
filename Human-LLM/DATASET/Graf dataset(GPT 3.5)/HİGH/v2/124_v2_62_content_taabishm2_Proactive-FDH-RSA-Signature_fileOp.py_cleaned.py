import os
b1 = os.getcwd() + "\\RSAfiles\\"
def fonk1(filename, lst):
    '''Write a list 'lst' into a file named 'filename.txt'.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'w') as file:
        file.write(','.join(map(str, lst)))
def fonk2(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of integers.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return [int(x) for x in b3]
def fonk3(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of non-integers.'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return b3
def fonk4(filename):
    '''Read data from a large file named 'filename.txt'.'''
    b4 = ""
    with open(b1 + filename + ".txt") as infile:
        for line in infile:
            b4 += line
    return b4
def fonk5(filename):
    '''Read data from a binary file named 'filename'.'''
    b4 = ""
    with open(b1 + filename, 'rb') as infile:
        for line in infile:
            b4 += str(line)
    return b4
