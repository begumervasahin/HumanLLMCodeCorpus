import os
SAVE_PATH = os.getcwd() + "\\RSAfiles\\"
def write_list_to_file(filename, lst):
    '''Write a list 'lst' into a file named 'filename.txt'.'''
    file_path = SAVE_PATH + filename + '.txt'
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, lst)))
def read_list_from_file(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of integers.'''
    file_path = SAVE_PATH + filename + '.txt'
    with open(file_path, 'r') as file:
        data = file.read().split(',')
    return [int(x) for x in data]
def read_list_from_file_non_int(filename):
    '''Read data from a file named 'filename.txt' and return it as a list of non-integers.'''
    file_path = SAVE_PATH + filename + '.txt'
    with open(file_path, 'r') as file:
        data = file.read().split(',')
    return data
def read_large_data_from_file(filename):
    '''Read data from a large file named 'filename.txt'.'''
    file_path = SAVE_PATH + filename + ".txt"
    with open(file_path) as file:
        data = file.read()
    return data
def read_binary_file(filename):
    '''Read data from a binary file named 'filename'.'''
    file_path = SAVE_PATH + filename
    with open(file_path, 'rb') as file:
        data = file.read()
    return data
