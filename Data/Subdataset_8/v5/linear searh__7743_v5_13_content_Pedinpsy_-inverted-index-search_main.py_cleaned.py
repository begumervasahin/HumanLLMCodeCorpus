import os
import re
import time
from hash import HashTable
def read_directory(directory):
    files = [os.path.join(directory, name) for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    return files
def clean_text(text):
    cleaned_text = re.sub(r'[,.!?\r\t\n]', '', text.lower())
    return cleaned_text.split()
def generate_index(file_path, index, file_number):
    with open(file_path, 'r') as file:
        words = clean_text(file.read())
    for word in words:
        count = words.count(word)
        flag = True
        if index.get_value(word):
            for entry in index.get_value(word):
                if entry[0] == count and entry[1] == file_number + 1:
                    flag = False
            if flag:
                index.insert_value(word, [count, file_number + 1])
        else:
            index.insert_value(word, [count, file_number + 1])
def print_index(index, files):
    for key in sorted(index.get_keys()):
        file_index = index.get_value(key)[0][1] - 1
        print(key, index.get_value(key)[0][0], files[file_index])
def calculate_time(start_time):
    return time.time() - start_time
hashing_multiplication_linear = HashTable(1000000, 3, 'multiplication')
hashing_multiplication_quadratic = HashTable(1000000, 3, 'multiplication', 'quadratic')
hashing_division_linear = HashTable(1000000, 3)
hashing_division_quadratic = HashTable(1000000, 3, 'division', 'linear')
start_time = time.time()
files = read_directory('base')
for i, file_path in enumerate(files):
    generate_index(file_path, hashing_multiplication_linear, i)
print_index(hashing_multiplication_linear, files)
print('Time taken for hashing using multiplication method and linear collision:', calculate_time(start_time))
start_time = time.time()
files = read_directory('base')
for i, file_path in enumerate(files):
    generate_index(file_path, hashing_multiplication_quadratic, i)
print_index(hashing_multiplication_quadratic, files)
print('Time taken for hashing using multiplication method and quadratic collision:', calculate_time(start_time))
start_time = time.time()
files = read_directory('base')
for i, file_path in enumerate(files):
    generate_index(file_path, hashing_division_linear, i)
print_index(hashing_division_linear, files)
print('Time taken for hashing using division method and linear collision:', calculate_time(start_time))
start_time = time.time()
files = read_directory('base')
for i, file_path in enumerate(files):
    generate_index(file_path, hashing_division_quadratic, i)
print_index(hashing_division_quadratic, files)
print('Time taken for hashing using division method and quadratic collision:', calculate_time(start_time))
while True:
    word = input("Enter a word:\n")
    print(hashing_multiplication_linear.get_value(word))