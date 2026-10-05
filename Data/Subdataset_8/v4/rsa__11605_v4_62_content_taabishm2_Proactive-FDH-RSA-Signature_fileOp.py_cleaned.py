import os
save_path = os.getcwd() + "\RSAfiles\\"
def write_list(filename, l):
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'w') as file:
        file.write(','.join(map(str, l)))
def read_list(filename):
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'r') as file:
        arr = file.read().split(',')
        return list(map(int, arr))
def read_list_noint(filename):
    complete_name = save_path + filename + '.txt'
    with open(complete_name, 'r') as file:
        arr = file.read().split(',')
        return arr
def read_large_data(filename):
    msg = ""
    with open(save_path + filename + ".txt") as infile:
        for line in infile:
            msg += line
    return msg
def read_binary_file(filename):
    msg = ""
    with open(save_path + filename, 'rb') as infile:
        for line in infile:
            msg += str(line)
    return msg