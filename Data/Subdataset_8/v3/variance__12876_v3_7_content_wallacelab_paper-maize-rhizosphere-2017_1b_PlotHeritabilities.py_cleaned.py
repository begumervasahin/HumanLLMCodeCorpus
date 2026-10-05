import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def main():
    args = parse_arguments()
    print("Plotting heritabilities from", args.infile)
    data = pd.read_csv(args.infile, sep='\t')
    sorted_columns = sort_columns_by_heritability(data)
    data = data.iloc[:, sorted_columns]
    plot_heritabilities(data, args.outfile)
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="Input file containing heritability data")
    parser.add_argument("-o", "--outfile", help="Output file to save the plot")
    parser.add_argument("--debug", default=False, action="store_true")
    return parser.parse_args()
def sort_columns_by_heritability(data):
    return np.argsort(data.loc['actual', :])[::-1]
def plot_heritabilities(data, outfile):
    fig = plt.figure(figsize=(calculate_figure_width(data), 5))
    grid = gridspec.GridSpec(nrows=100, ncols=100)
    ax = fig.add_subplot(grid[:80, :], title="Distributions of null heritabilities", xlabel="Trait", ylabel="Heritability")
    xticks, xlabels = [], []
    for x, trait in enumerate(data.columns):
        xticks.append(x)
        ax.violinplot(data.loc[data.index != 'actual', trait], positions=[x])
        xlabels.append(trait.replace("trait_", ""))
    ax.scatter(xticks, data.loc['actual', :])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation="vertical")
    fig.savefig(outfile, dpi=100)
def calculate_figure_width(data):
    return 5 + .25 * len(data.columns)
if __name__ == '__main__':
    main()