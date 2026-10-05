import os
save_path = os.getcwd() + "\\RSAfiles\\"
def write_list(filename, lst):
    '''Write a list 'lst' into a file named 'filename.txt'.'''
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'w') as file:
        file.write(','.join(map(str, lst)))
def read_list(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of integers.'''
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'r') as file:
        arr = file.read().split(',')
    return [int(x) for x in arr]
def read_list_noint(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of non-integers.'''
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'r') as file:
        arr = file.read().split(',')
    return arr
def read_large_data(filename):
    '''Read data from a large file named 'filename.txt'.'''
    msg = ""
    with open(save_path + filename + ".txt") as infile:
        for line in infile:
            msg += line
    return msg
def read_binary_file(filename):
    '''Read data from a binary file named 'filename'.'''
    msg = ""
    with open(save_path + filename, 'rb') as infile:
        for line in infile:
            msg += str(line)
    return msg
