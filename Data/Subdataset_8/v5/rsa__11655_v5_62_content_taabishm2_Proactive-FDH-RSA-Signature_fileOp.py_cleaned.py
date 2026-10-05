import os
SAVE_PATH = os.path.join(os.getcwd(), "RSAfiles")
def write_list_to_file(filename, data_list):
    file_path = os.path.join(SAVE_PATH, f"{filename}.txt")
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, data_list)))
def read_list_from_file(filename, read_as_int=True):
    file_path = os.path.join(SAVE_PATH, f"{filename}.txt")
    with open(file_path, 'r') as file:
        data = file.read().split(',')
        if read_as_int:
            return list(map(int, data))
        else:
            return data
def read_large_data_from_file(filename):
    file_path = os.path.join(SAVE_PATH, f"{filename}.txt")
    with open(file_path) as file:
        return file.read()
def read_binary_file(filename):
    file_path = os.path.join(SAVE_PATH, filename)
    with open(file_path, 'rb') as file:
        return file.read().decode('utf-8')