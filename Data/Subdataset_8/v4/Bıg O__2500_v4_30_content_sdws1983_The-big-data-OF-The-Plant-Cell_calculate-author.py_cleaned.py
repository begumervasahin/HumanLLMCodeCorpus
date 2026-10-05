import sys
import getopt
import re
import time
import pandas as pd
import os
def get_option():
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    input_file = ""
    output_file = ""
    h = ""
    for op, value in opts:
        if op == "-i":
            input_file = value
        elif op == "-o":
            output_file = value
        elif op == "-h":
            h = 'usage:\nremove the sequence which contains "N"\n-i : inputfile\n-o : outputfile\n'
    return input_file, output_file, h
def main(input_file, output_file):
    all_sequences = []
    with open(input_file) as f:
        for line in f:
            if line[0] != ">":
                all_sequences.append(line.strip())
    print("Total sequences:", len(all_sequences))
    tag_counts = {}
    for sequence in all_sequences:
        if sequence not in tag_counts.keys():
            tag_counts[sequence] = 1
        else:
            tag_counts[sequence] += 1
    print("Tag counts:", tag_counts)
    with open('tmp.txt', 'w') as fout:
        for tag, count in tag_counts.items():
            line = f"{tag}\t{count}\n"
            fout.write(line)
    data = pd.DataFrame(pd.read_table('tmp.txt', names=['sequence', 'count']))
    data = data.sort_values(by=['count'], ascending=False)
    data.to_csv(output_file, sep='\t', index=False)
    os.remove('tmp.txt')
if __name__ == "__main__":
    time_start = time.time()
    input_file, output_file, h = get_option()
    if h == "":
        main(input_file, output_file)
        print("Time taken:", time.time() - time_start)
    else:
        print(h)