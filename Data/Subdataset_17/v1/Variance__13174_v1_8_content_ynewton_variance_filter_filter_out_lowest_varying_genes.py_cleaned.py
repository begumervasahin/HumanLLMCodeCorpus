import argparse
import sys
import numpy as np
import math
def main():
    parser = argparse.ArgumentParser(description="Filter genes based on variance")
    parser.add_argument("--in_file", required=True, help="Input file")
    parser.add_argument("--filter_level", required=True, type=float, help="Filter level (must be a float below 1)")
    parser.add_argument("--out_file", required=True, help="Output file")
    args = parser.parse_args()
    in_file = args.in_file
    filter_level = args.filter_level
    out_file_name = args.out_file
    if not (0 <= filter_level <= 1):
        sys.stderr.write("ERROR: --filter_level must be in interval [0,1].\n")
        sys.exit(1)
    sys.stderr.write("Reading in input...\n")
    line_count = 1
    variance = []
    genes = []
    with open(in_file, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line_count > 1:
                line_elems = line.split("\t")
                genes.append(line_elems[0])
                line_float = [float(x) for x in line_elems[1:]]
                variance.append(np.std(np.array(line_float)))
            line_count += 1
    sys.stderr.write("Sorting on variance...\n")
    cut_proportion = int(math.ceil(len(variance) * filter_level))
    var_dict = dict(zip(genes, variance))
    sorted_tuples = sorted(var_dict.items(), key=lambda x: x[1])
    sorted_tuples_filtered = sorted_tuples[cut_proportion:]
    sorted_var_dict = {x: y for x, y in sorted_tuples_filtered}
    valid_genes = set(sorted_var_dict.keys())
    sys.stderr.write("Outputting filtered data...\n")
    line_count = 1
    with open(in_file, 'r') as input_file, open(out_file_name, 'w') as output_file:
        for line in input_file:
            line = line.strip()
            if line_count == 1:
                output_file.write(line + "\n")
            else:
                line_elems = line.split("\t")
                if line_elems[0] in valid_genes:
                    output_file.write(line + "\n")
            line_count += 1
if __name__ == "__main__":
    main()