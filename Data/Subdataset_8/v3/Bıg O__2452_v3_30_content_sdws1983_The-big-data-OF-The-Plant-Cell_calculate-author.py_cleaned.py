import sys
import getopt
import pandas as pd
import os
import time
def parse_command_line_arguments():
    input_file = ""
    output_file = ""
    help_message = ""
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hi:o:")
    except getopt.GetoptError:
        help_message = 'Usage:\nRemove the sequences which contain "N"\n-i: input file\n-o: output file\n'
        return "", "", help_message
    for option, value in opts:
        if option == "-i":
            input_file = value
        elif option == "-o":
            output_file = value
        elif option == "-h":
            help_message = 'Usage:\nRemove the sequences which contain "N"\n-i: input file\n-o: output file\n'
    return input_file, output_file, help_message
def remove_sequences_with_n(input_file, output_file):
    sequences = []
    with open(input_file, "r") as file:
        for line in file:
            if line[0] != ">":
                sequences.append(line.strip())
    sequence_counts = {}
    for sequence in sequences:
        if sequence not in sequence_counts:
            sequence_counts[sequence] = 1
        else:
            sequence_counts[sequence] += 1
    with open('tmp.txt', 'w') as tmp_file:
        for seq, count in sequence_counts.items():
            tmp_file.write(f"{seq}\t{count}\n")
    data = pd.read_csv('tmp.txt', sep='\t', names=['Sequence', 'Count'])
    sorted_data = data.sort_values(by='Count', ascending=False)
    sorted_data.to_csv(output_file, sep='\t', index=False)
    os.remove('tmp.txt')
if __name__ == "__main__":
    start_time = time.time()
    input_file, output_file, help_message = parse_command_line_arguments()
    if help_message:
        print(help_message)
    else:
        remove_sequences_with_n(input_file, output_file)
        print("Time elapsed:", time.time() - start_time)