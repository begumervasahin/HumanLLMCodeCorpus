from collections import deque
def column_break(test):
    c = []
    letters = []
    k = 0
    for j in range(4):
        for i in range(4):
            letters.append(test[(8 * i) + k:(8 * i) + 2 + k])
        k += 2
        c.append(letters)
        letters = []
    return c
def byte_to_array(bytes_string):
    array = []
    for i, byte in enumerate(bytes_string):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i
    return array
def get_key_schedule(key):
    W = []
    keys = byte_to_array(bytes.fromhex(key))
    for j in range(4, 44):
        x0 = keys[j - 4][0]
        x1 = keys[j - 4][1]
        x2 = keys[j - 4][2]
        x3 = keys[j - 4][3]
        fren = [x3, x0, x1, x2]
        keys.append(fren)
    return keys
key1 = "7750f228896eb4561b9cd67497aad0b1"
master = get_key_schedule(key1)
print("Length of master key schedule:", len(master))