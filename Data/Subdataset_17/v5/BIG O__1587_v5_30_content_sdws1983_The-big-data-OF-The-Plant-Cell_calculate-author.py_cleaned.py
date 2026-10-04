import sys
import getopt
import pandas as pd
import os
import time
def print_usage():
    usage_message = (
        "Usage:\n"
        "Remove the sequences that contain 'N'\n"
        "-i : input file\n"
        "-o : output file\n"
    )
    print(usage_message)
def get_options():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hi:o:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    input_file = ""
    output_file = ""
    show_usage = False
    for opt, value in opts:
        if opt == "-i":
            input_file = value
        elif opt == "-o":
            output_file = value
        elif opt == "-h":
            show_usage = True
    return input_file, output_file, show_usage
def read_sequences(input_file):
    sequences = []
    with open(input_file) as f:
        for line in f:
            if not line.startswith(">"):
                sequences.append(line.strip())
    return sequences
def count_sequences(sequences):
    sequence_counts = {}
    for seq in sequences:
        if seq in sequence_counts:
            sequence_counts[seq] += 1
        else:
            sequence_counts[seq] = 1
    return sequence_counts
def save_to_file(sequence_counts, output_file):
    temp_file = 'tmp.txt'
    with open(temp_file, 'w') as f:
        for seq, count in sequence_counts.items():
            f.write(f"{seq}\t{count}\n")
    data = pd.read_csv(temp_file, sep='\t', names=['Sequence', 'Count'])
    sorted_data = data.sort_values(by='Count', ascending=False)
    sorted_data.to_csv(output_file, sep='\t', index=False)
    os.remove(temp_file)
def main(input_file, output_file):
    sequences = read_sequences(input_file)
    print(f"Total sequences: {len(sequences)}")
    sequence_counts = count_sequences(sequences)
    print(f"Unique sequences: {len(sequence_counts)}")
    save_to_file(sequence_counts, output_file)
if __name__ == "__main__":
    start_time = time.time()
    input_file, output_file, show_usage = get_options()
    if show_usage or not input_file or not output_file:
        print_usage()
    else:
        main(input_file, output_file)
        elapsed_time = time.time() - start_time
        print(f"Time elapsed: {elapsed_time:.2f} seconds")