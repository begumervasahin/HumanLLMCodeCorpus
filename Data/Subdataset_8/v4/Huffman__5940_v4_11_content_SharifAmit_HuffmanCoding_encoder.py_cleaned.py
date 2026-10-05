
file = open("input.txt", "r")
input_string = file.readline().lower()
unique_chars = list(set(input_string))
print("The String:", input_string)
print("The unique characters:", unique_chars)
frequency_table = [0] * len(unique_chars)
for char in input_string:
    count = input_string.count(char)
    index = unique_chars.index(char)
    if frequency_table[index] == 0:
        frequency_table[index] = count
print("Frequency Table before sorting:")
print(frequency_table)
sorted_frequency = []
sorted_chars = []
while frequency_table:
    max_freq = max(frequency_table)
    max_index = frequency_table.index(max_freq)
    sorted_frequency.append(max_freq)
    sorted_chars.append(unique_chars[max_index])
    frequency_table.pop(max_index)
    unique_chars.pop(max_index)
print("Frequency Table after sorting:")
print(sorted_frequency)
print(sorted_chars)
leaf_count = sum(1 for freq in sorted_frequency if freq != 0)
node_count = 2 * leaf_count - 1
print("Number of nodes in the tree:", node_count)
print("Number of leafs in the tree:", leaf_count)
encoder = ["null"] * leaf_count
print("Encoder:", encoder)
binary_tree = list(sorted_frequency)
string_tree = list(sorted_chars)
print("Binary Tree:", binary_tree)
print("String Tree:", string_tree)
for _ in range(len(binary_tree) - 1, -1, -1):
    left = 999
    right = 999
    left_str = ""
    right_str = ""
    for i in range(len(binary_tree) - 1, -1, -1):
        if binary_tree[i] < right:
            right = binary_tree[i]
            right_str = string_tree[i]
    for char in right_str:
        char_index = sorted_chars.index(char)
        if encoder[char_index] == "null":
            encoder[char_index] = "0"
        else:
            encoder[char_index] = "0" + encoder[char_index]
    right_index = string_tree.index(right_str)
    string_tree.pop(right_index)
    binary_tree.pop(right_index)
    for i in range(len(binary_tree) - 1, -1, -1):
        if binary_tree[i] < left or binary_tree[i] == right:
            left = binary_tree[i]
            left_str = string_tree[i]
    for char in left_str:
        char_index = sorted_chars.index(char)
        if encoder[char_index] == "null":
            encoder[char_index] = "1"
        else:
            encoder[char_index] = "1" + encoder[char_index]
    left_index = string_tree.index(left_str)
    string_tree.pop(left_index)
    binary_tree.pop(left_index)
    summation = right + left
    combined_str = left_str + right_str
    string_tree.insert(0, combined_str)
    binary_tree.insert(0, summation)
    if len(binary_tree) == 1:
        break
print("Encoder after Huffman coding:", encoder)
print("Character list:", sorted_chars)
encoded_string = ""
for char in input_string:
    char_index = sorted_chars.index(char)
    encoded_string += encoder[char_index]
print("Encoded string:", encoded_string)
output_file = open("output.txt", "w")
output_file.write(encoded_string)
output_file.close()
dictionary_file = open("dictionary.txt", "w")
for i in range(len(encoder)):
    char = sorted_chars[i]
    code = encoder[i]
    dictionary_entry = char + "=" + code
    print(dictionary_entry)
    dictionary_file.write(dictionary_entry + "\n")
dictionary_file.close()
file.close()