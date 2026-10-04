
from sys import argv, exit
from os.path import isfile
LENGTH = 0
NAME = 0
SEQUENCE = 1
def die(message=None, code=1):
    if message:
        print(f"Error: {message}")
    else:
        print("Error: An Undefined Error Occurred!")
    exit(code)
def get_sequences_from_file(filename):
    try:
        with open(filename, "r") as f:
            file_string = f.read()
    except IOError:
        die(f"Error! Could not open {filename}")
    sequences = file_string.strip().split("\n\n")
    if not sequences or sequences[0][0] != '>':
        die("Could not find any sequences!")
    return [get_sequence_data(seq) for seq in sequences if seq]
def lcs(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    lcs_array = [[""] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                lcs_array[i][j] = lcs_array[i - 1][j - 1] + seq1[i - 1]
            else:
                lcs_array[i][j] = max(lcs_array[i - 1][j], lcs_array[i][j - 1], key=len)
    lcs_str = lcs_array[len1][len2]
    return len(lcs_str), lcs_str
def get_sequence_data(sequence):
    name, sequence = sequence.split('\n', 1)
    name = name[1:]
    sequence = sequence.replace("\n", "")
    return name, sequence
def get_sequence_max_lcs(sequence_dict):
    max_lcs = 0
    max_lcs_object = None
    for key, seq_data in sequence_dict.items():
        if seq_data[LENGTH] > max_lcs:
            max_lcs = seq_data[LENGTH]
            max_lcs_object = (key, seq_data)
    return max_lcs_object
def add_to_group(name, to_add, groups):
    if name not in groups:
        groups[name] = []
    groups[name].append(to_add)
def get_grouped_sequences(sequences):
    groups = {}
    for sequence in sequences:
        max_sequence_name, max_sequence_object = get_sequence_max_lcs(sequences[sequence])
        to_add = (sequence, max_sequence_object[LENGTH], max_sequence_object[SEQUENCE])
        add_to_group(max_sequence_name, to_add, groups)
    return groups
def get_filename(args):
    if len(args) < 2:
        filename = input("Please enter the filename containing protein sequences: ")
    else:
        filename = args[1]
    if not isfile(filename):
        die(f"Could not find file '{filename}'")
    return filename
def lcs_all_sequences(sequences):
    lcs_dict = {name: {} for name, _ in sequences}
    num_sequences = len(sequences)
    for idx, (name1, seq1) in enumerate(sequences):
        print(f"[{idx + 1}/{num_sequences}] {name1}...")
        for name2, seq2 in sequences[idx + 1:]:
            lcs_data = lcs(seq1, seq2)
            lcs_dict[name1][name2] = lcs_dict[name2][name1] = lcs_data
            print(f"   {name2}... LCS Length: {lcs_data[LENGTH]}")
        print()
    return lcs_dict
def print_grouped_item(item, padding=2, offset=20):
    padded = " " * padding
    name_string = f"Name: {item[NAME]}"
    offset = max(offset - len(name_string), 0) * " "
    print(f"{padded}{name_string} {offset}Length of LCS: {item[1]}")
def main(args):
    filename = get_filename(args)
    sequences = get_sequences_from_file(filename)
    lcs_sequence_dict = lcs_all_sequences(sequences)
    grouped_sequences = get_grouped_sequences(lcs_sequence_dict)
    for group in grouped_sequences:
        print(f"Group {group}:")
        for grouped_item in grouped_sequences[group]:
            print_grouped_item(grouped_item)
if __name__ == "__main__":
    main(argv)