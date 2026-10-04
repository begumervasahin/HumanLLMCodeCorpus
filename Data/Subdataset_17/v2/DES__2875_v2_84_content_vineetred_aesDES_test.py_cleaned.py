from collections import deque
def column_break(input_str):
    columns = []
    k = 0
    for _ in range(4):
        column = []
        for i in range(4):
            segment = input_str[(8 * i) + k : (8 * i) + 2 + k]
            column.append(segment)
        k += 2
        columns.append(column)
    return columns
def bytes_to_array(byte_data):
    array = []
    for i, byte in enumerate(byte_data):
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
if __name__ == "__main__":
    key = "7750f228896eb4561b9cd67497aad0b1"
    key_schedule = get_key_schedule(key)
    print(f"Key Schedule Length: {len(key_schedule)}")
    test_string = "example string for column break"
    columns = column_break(test_string)
    print("Columns:")
    for col in columns:
        print(col)