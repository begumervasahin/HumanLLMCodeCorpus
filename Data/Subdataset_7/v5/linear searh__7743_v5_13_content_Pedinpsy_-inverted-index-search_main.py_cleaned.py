import os
import re
import time
from hash import HashTable
def fonk1(directory):
    b1 = [os.path.join(directory, name) for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
    return b1
def fonk2(text):
    b2 = re.sub(r'[,.!?\r\t\n]', '', text.lower())
    return b2.split()
def fonk3(file_path, index, file_number):
    with open(file_path, 'r') as file:
        b3 = fonk2(file.read())
    for b12 in b3:
        b4 = b3.b4(b12)
        b5 = True
        if index.get_value(b12):
            for entry in index.get_value(b12):
                if entry[0] == b4 and entry[1] == file_number + 1:
                    b5 = False
            if b5:
                index.insert_value(b12, [b4, file_number + 1])
        else:
            index.insert_value(b12, [b4, file_number + 1])
def fonk4(index, b1):
    for key in sorted(index.get_keys()):
        b6 = index.get_value(key)[0][1] - 1
        print(key, index.get_value(key)[0][0], b1[b6])
def fonk5(b11):
    return time.time() - b11
b7 = HashTable(1000000, 3, 'multiplication')
b8 = HashTable(1000000, 3, 'multiplication', 'quadratic')
b9 = HashTable(1000000, 3)
b10 = HashTable(1000000, 3, 'division', 'linear')
b11 = time.time()
b1 = fonk1('base')
for i, file_path in enumerate(b1):
    fonk3(file_path, b7, i)
fonk4(b7, b1)
print('Time taken for hashing using multiplication method and linear collision:', fonk5(b11))
b11 = time.time()
b1 = fonk1('base')
for i, file_path in enumerate(b1):
    fonk3(file_path, b8, i)
fonk4(b8, b1)
print('Time taken for hashing using multiplication method and quadratic collision:', fonk5(b11))
b11 = time.time()
b1 = fonk1('base')
for i, file_path in enumerate(b1):
    fonk3(file_path, b9, i)
fonk4(b9, b1)
print('Time taken for hashing using division method and linear collision:', fonk5(b11))
b11 = time.time()
b1 = fonk1('base')
for i, file_path in enumerate(b1):
    fonk3(file_path, b10, i)
fonk4(b10, b1)
print('Time taken for hashing using division method and quadratic collision:', fonk5(b11))
while True:
    b12 = input("Enter a b12:\n")
    print(b7.get_value(b12))