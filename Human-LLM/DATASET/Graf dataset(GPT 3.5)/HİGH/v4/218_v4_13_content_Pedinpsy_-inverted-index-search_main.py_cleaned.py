import os
import re
import time
from hash import HashTable
def fonk1(directory):
    b1 = [os.path.join(directory, name) for name in os.listdir(directory)]
    b2 = [file for file in b1 if os.path.isfile(file)]
    return b2
def fonk2(file_path, index, num):
    with open(file_path, 'r') as file:
        b3 = file.read().lower()
    b3 = re.sub(r'[,.!?\r\t\n]', '', b3)
    b3 = b3.split(" ")
    for b12 in b3:
        b4 = b3.b4(b12)
        b5 = True
        if index.get_value(b12):
            for entry in index.get_value(b12):
                if entry[0] == b4 and entry[1] == num + 1:
                    b5 = False
            if b5:
                index.insert_value(b12, [b4, num + 1])
        else:
            index.insert_value(b12, [b4, num + 1])
b6 = HashTable(1000000, 3, 'multiplication')
b7 = HashTable(1000000, 3, 'multiplication', 'quadratic')
b8 = HashTable(1000000, 3)
b9 = HashTable(1000000, 3, 'division', 'linear')
b10 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
    fonk2(b2[i], b6, i)
for key in sorted(b6.get_keys()):
    print(key, b6.get_value(key)[0][0], b2[(b6.get_value(key)[0][1]) - 1])
b11 = time.time()
print('Time taken for hashing using multiplication method and linear collision:', b11 - b10)
b10 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
    fonk2(b2[i], b7, i)
for key in sorted(b7.get_keys()):
    print(key, b7.get_value(key)[0][0], b2[(b7.get_value(key)[0][1]) - 1])
b11 = time.time()
print('Time taken for hashing using multiplication method and quadratic collision:', b11 - b10)
b10 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
    fonk2(b2[i], b8, i)
for key in sorted(b8.get_keys()):
    print(key, b8.get_value(key)[0][0], b2[(b8.get_value(key)[0][1]) - 1])
b11 = time.time()
print('Time taken for hashing using division method and linear collision:', b11 - b10)
b10 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
    fonk2(b2[i], b9, i)
for key in sorted(b9.get_keys()):
    print(key, b9.get_value(key)[0][0], b2[(b9.get_value(key)[0][1]) - 1])
b11 = time.time()
print('Time taken for hashing using division method and quadratic collision:', b11 - b10)
while True:
    b12 = input("Enter a b12:\n")
    print(b6.get_value(b12))