
with open("input.txt", "r") as file:
    original_string = file.readline().lower()
unique_chars = list(set(original_string))
print("The String:", original_string)
print("The char list:", unique_chars)
char_frequencies = [0] * len(unique_chars)
for char in original_string:
    count = original_string.count(char)
    char_index = unique_chars.index(char)
    if char_frequencies[char_index] == 0:
        char_frequencies[char_index] = count
print("Frequency Table before sorting:")
print(char_frequencies)
sorted_frequencies = []
sorted_chars = []
while char_frequencies:
    max_freq = max(char_frequencies)
    index = char_frequencies.index(max_freq)
    sorted_frequencies.append(max_freq)
    sorted_chars.append(unique_chars[index])
    char_frequencies.pop(index)
    unique_chars.pop(index)
print("Frequency Table after sorting:")
print(sorted_frequencies)
print(sorted_chars)
num_nodes = sum(1 for freq in sorted_frequencies if freq != 0)
num_leafs = 2 * num_nodes - 1
print("Number of nodes in the tree:", num_leafs)
print("Number of leafs in the tree:", num_nodes)
encoder = ["null"] * num_nodes
binary_tree = list(sorted_frequencies)
string_tree = list(sorted_chars)
while len(binary_tree) > 1:
    right_freq = min(binary_tree)
    right_char = string_tree[binary_tree.index(right_freq)]
    binary_tree.remove(right_freq)
    string_tree.remove(right_char)
    left_freq = min(binary_tree)
    left_char = string_tree[binary_tree.index(left_freq)]
    binary_tree.remove(left_freq)
    string_tree.remove(left_char)
    total_freq = right_freq + left_freq
    total_char = left_char + right_char
    string_tree.append(total_char)
    binary_tree.append(total_freq)
    for char in right_char:
        char_index = sorted_chars.index(char)
        encoder[char_index] = "0" + encoder[char_index]
    for char in left_char:
        char_index = sorted_chars.index(char)
        encoder[char_index] = "1" + encoder[char_index]
print("Encoder:", encoder)
encoded_string = ""
for char in original_string:
    char_index = sorted_chars.index(char)
    encoded_string += encoder[char_index]
print("Encoded String:", encoded_string)
with open("output.txt", "w") as output_file:
    output_file.write(encoded_string)
with open("dictionary.txt", "w") as dict_file:
    for i in range(len(encoder)):
        char = sorted_chars[i]
        code = encoder[i]
        entry = char + "=" + code
        print(entry)
        dict_file.write(entry + "\n")