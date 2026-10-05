from collections import deque
def column_break(input_string):
    columns = []
    letters = []
    index = 0
    for _ in range(4):
        for _ in range(4):
            letters.append(input_string[index:index + 2])
            index += 2
        columns.append(letters)
        letters = []
    return columns
def bytes_to_array(bytes_string):
    array = []
    for i, byte in enumerate(bytes_string):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i
    return array
def generate_key_schedule(key):
    key_schedule = []
    keys = bytes_to_array(bytes.fromhex(key))
    for _ in range(4, 44):
        x0, x1, x2, x3 = keys[-4]
        round_key = [x3, x0, x1, x2]
        keys.append(round_key)
    return keys
key = "7750f228896eb4561b9cd67497aad0b1"
key_schedule = generate_key_schedule(key)
print("Length of key schedule:", len(key_schedule))