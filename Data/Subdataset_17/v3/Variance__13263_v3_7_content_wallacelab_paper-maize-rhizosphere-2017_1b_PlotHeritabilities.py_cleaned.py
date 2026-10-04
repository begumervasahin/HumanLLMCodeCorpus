import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def main():
    args = parse_args()
    print(f"Plotting heritabilities from {args.infile}")
    data = load_and_order_data(args.infile)
    create_plot(data, args.outfile)
def parse_args():
    parser = argparse.ArgumentParser(description="Plot heritabilities from a given input file.")
    parser.add_argument("-i", "--infile", required=True, help="Input file containing heritabilities.")
    parser.add_argument("-o", "--outfile", required=True, help="Output file to save the plot.")
    parser.add_argument("--debug", default=False, action="store_true", help="Enable debug mode.")
    return parser.parse_args()
def load_and_order_data(infile):
    data = pd.read_csv(infile, sep='\t')
    ordered_columns = np.argsort(data.loc['actual', :])[::-1]
    return data.iloc[:, ordered_columns]
def create_plot(data, outfile):
    fig, ax = plt.subplots(figsize=(5 + 0.25 * len(data.columns), 5))
    ax.set_title("Distributions of null heritabilities")
    ax.set_xlabel("Trait")
    ax.set_ylabel("Heritability")
    perms = data.index != "actual"
    xticks, xlabels = [], []
    for x, trait in enumerate(data.columns):
        xticks.append(x)
        ax.violinplot(data.loc[perms, trait], positions=[x])
        xlabels.append(trait.replace("trait_", ""))
    ax.scatter(xticks, data.loc['actual', :], color='red')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation="vertical")
    fig.savefig(outfile, dpi=100)
if __name__ == '__main__':
    main()