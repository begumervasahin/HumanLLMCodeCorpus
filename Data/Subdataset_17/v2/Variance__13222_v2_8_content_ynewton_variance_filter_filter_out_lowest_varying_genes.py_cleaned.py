import argparse
import sys
import numpy as np
import math
def main():
    parser = argparse.ArgumentParser(description="Filter genes based on variance")
    parser.add_argument("--in_file", required=True, help="Input file containing gene expression data")
    parser.add_argument("--filter_level", required=True, type=float, help="Filter level as a float between 0 and 1")
    parser.add_argument("--out_file", required=True, help="Output file to save filtered data")
    args = parser.parse_args()
    in_file = args.in_file
    filter_level = args.filter_level
    out_file_name = args.out_file
    if not (0 <= filter_level <= 1):
        sys.stderr.write("ERROR: --filter_level must be in interval [0,1].\n")
        sys.exit(1)
    sys.stderr.write("Reading in input...\n")
    variance = []
    genes = []
    with open(in_file, 'r') as input_file:
        for line_count, line in enumerate(input_file, start=1):
            line = line.strip()
            if line_count > 1:
                line_elems = line.split("\t")
                genes.append(line_elems[0])
                line_float = [float(x) for x in line_elems[1:]]
                variance.append(np.std(np.array(line_float)))
    sys.stderr.write("Sorting on variance...\n")
    cut_proportion = int(math.ceil(len(variance) * filter_level))
    var_dict = dict(zip(genes, variance))
    sorted_tuples = sorted(var_dict.items(), key=lambda x: x[1])
    sorted_tuples_filtered = sorted_tuples[cut_proportion:]
    sorted_var_dict = {gene: var for gene, var in sorted_tuples_filtered}
    valid_genes = set(sorted_var_dict.keys())
    sys.stderr.write("Outputting filtered data...\n")
    with open(in_file, 'r') as input_file, open(out_file_name, 'w') as output_file:
        for line_count, line in enumerate(input_file, start=1):
            line = line.strip()
            if line_count == 1:
                output_file.write(line + "\n")
            else:
                line_elems = line.split("\t")
                if line_elems[0] in valid_genes:
                    output_file.write(line + "\n")
if __name__ == "__main__":
    main()