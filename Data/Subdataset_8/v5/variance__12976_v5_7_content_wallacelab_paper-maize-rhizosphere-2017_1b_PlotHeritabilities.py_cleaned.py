import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
debug = False
def main():
    args = parse_args()
    print("Plotting heritabilities from", args.infile)
    data = pd.read_csv(args.infile, sep='\t')
    data = sort_data_columns(data)
    fig, ax = create_plot_figure(data)
    plot_data(ax, data)
    save_figure(fig, args.outfile)
def sort_data_columns(data):
    order = np.argsort(data.loc['actual', :])[::-1]
    return data.iloc[:, order]
def create_plot_figure(data):
    fig_width = 5 + .25 * len(data.columns)
    fig_height = 5
    fig = plt.figure(figsize=(fig_width, fig_height))
    grid = gridspec.GridSpec(nrows=100, ncols=100)
    ax = fig.add_subplot(grid[:80, :], title="Distributions of null heritabilities", xlabel="trait", ylabel="Heritability")
    return fig, ax
def plot_data(ax, data):
    perms = data.index != "actual"
    xticks, xlabels = [], []
    for x, trait in enumerate(data.columns):
        xticks.append(x)
        ax.violinplot(data.loc[perms, trait], positions=[x])
        xlabels.append(trait.replace("trait_", ""))
    ax.scatter(xticks, data.loc['actual', :])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation="vertical")
def save_figure(fig, outfile):
    fig.savefig(outfile, dpi=100)
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="Input file")
    parser.add_argument("-o", "--outfile", help="Output file")
    parser.add_argument("--debug", default=False, action="store_true", help="Enable debugging")
    args = parser.parse_args()
    global debug
    debug = args.debug
    return args
if __name__ == '__main__':
    main()