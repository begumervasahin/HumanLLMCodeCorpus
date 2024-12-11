import os
b1 = os.getcwd() + "\\RSAfiles\\"
def fonk1(filename, l):
    '''Write a list l into a file'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'w') as file:
        file.write(','.join(map(str, l)))
def fonk2(filename):
    '''Return data from file read as list, READS ONLY INTEGERS'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return [int(x) for x in b3]
def fonk3(filename):
    '''Return data from file read as list, READS NON INTEGERS'''
    b2 = b1 + filename + '.txt'
    with open(b2, 'r') as file:
        b3 = file.read().split(',')
    return b3
def fonk4(filename):
    '''Read basic data from file'''
    b4 = ""
    with open(b1 + filename + ".txt") as infile:
        for line in infile:
            b4 += line
    return b4
def fonk5(filename):
    '''Reads binary file'''
    b4 = ""
    with open(b1 + filename, 'rb') as infile:
        for line in infile:
            b4 += str(line)
    return b4
