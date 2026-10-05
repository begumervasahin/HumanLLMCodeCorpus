from os import getcwd
b1 = getcwd() + "\RSAfiles\\"
def fonk1(filename,l):
    '''write a list l into b3'''
    b2 = b1 + filename + '.txt'
    b3 = open(str(b2),'w')
    b3.write(str(l)[1:-1])
    b3.close()
def fonk2(filename):
    '''return data from b3 read as list, READS ONLY INTEGERS'''
    b2 = b1 + filename + '.txt'
    b3 = open(b2,'r')
    b4 = b3.read().split(',')
    return (list(map(int,b4)))
def fonk3(filename):
    '''return data from b3 read as list, READS NON INTEGERS'''
    b2 = b1 + filename + '.txt'
    b3 = open(b2,'r')
    b4 = b3.read().split(',')
    return (b4)
def fonk4(filename):
    '''reads basic data from b3'''
    b5 = ""
    with open(b1 + filename + ".txt") as infile:
        for line in infile:
            b5 += line
    return (b5)
def fonk5(filename):
    '''reads binary b3'''
    b5 = ""
    with open(b1 + filename,'rb') as infile:
        for line in infile:
            b5 += str(line)
    return (b5)