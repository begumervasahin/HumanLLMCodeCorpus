import sys
import getopt
import time
import pandas as pd
import os
def print_usage():
    usage_info = (
        'Usage:\n'
        'Remove the sequences which contain "N".\n'
        '-i : inputfile\n'
        '-o : outputfile\n'
    )
    print(usage_info)
def get_options():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hi:o:")
        input_file, output_file = "", ""
        for op, value in opts:
            if op == "-i":
                input_file = value
            elif op == "-o":
                output_file = value
            elif op == "-h":
                print_usage()
                sys.exit()
        if not input_file or not output_file:
            print_usage()
            sys.exit()
        return input_file, output_file
    except getopt.GetoptError:
        print_usage()
        sys.exit()
def process_sequences(input_file, output_file):
    sequences = []
    with open(input_file, 'r') as f:
        for line in f:
            if not line.startswith(">"):
                sequences.append(line.strip())
    sequence_counts = {}
    for sequence in sequences:
        if sequence not in sequence_counts:
            sequence_counts[sequence] = 1
        else:
            sequence_counts[sequence] += 1
    tmp_file = 'tmp.txt'
    with open(tmp_file, 'w') as temp_out:
        for sequence, count in sequence_counts.items():
            temp_out.write(f"{sequence}\t{count}\n")
    data = pd.read_csv(tmp_file, sep='\t', names=['sequence', 'count'])
    data.sort_values(by='count', ascending=False, inplace=True)
    data.to_csv(output_file, sep='\t', index=False)
    os.remove(tmp_file)
def main():
    start_time = time.time()
    input_file, output_file = get_options()
    process_sequences(input_file, output_file)
    print(f"Execution time: {time.time() - start_time:.2f} seconds")
if __name__ == "__main__":
    main()