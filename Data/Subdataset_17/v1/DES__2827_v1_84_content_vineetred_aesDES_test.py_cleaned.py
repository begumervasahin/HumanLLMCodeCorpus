from collections import deque
def column_break(test):
    columns = []
    letters = []
    k = 0
    for j in range(4):
        for i in range(4):
            letters.append(test[(8 * i) + k : (8 * i) + 2 + k])
        k += 2
        columns.append(letters)
        letters = []
    return columns
def bytes_to_array(bytes_data):
    array = []
    for i, byte in enumerate(bytes_data):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i
    return array
def get_key_schedule(key):
    keys = bytes_to_array(bytes.fromhex(key))
    for j in range(4, 44):
        x0, x1, x2, x3 = keys[j - 4]
        rotated_word = [x3, x0, x1, x2]
        keys.append(rotated_word)
    return keys
key1 = "7750f228896eb4561b9cd67497aad0b1"
master_key_schedule = get_key_schedule(key1)
print(len(master_key_schedule))
test_string = "example string for column break"
columns = column_break(test_string)
print(columns)