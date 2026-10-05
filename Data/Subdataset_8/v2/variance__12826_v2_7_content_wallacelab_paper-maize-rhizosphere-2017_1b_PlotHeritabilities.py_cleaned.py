import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def main():
    args = parse_args()
    print("Plotting heritabilities from", args.infile)
    data = pd.read_csv(args.infile, sep='\t')
    sorted_columns = np.argsort(data.loc['actual', :])[::-1]
    data = data.iloc[:, sorted_columns]
    fig = plt.figure(figsize=(5 + .25 * len(data.columns), 5))
    grid = gridspec.GridSpec(nrows=100, ncols=100)
    ax = fig.add_subplot(grid[:80, :], title="Distributions of null heritabilities", xlabel="trait", ylabel="Heritability")
    xticks, xlabels = list(), list()
    for x in range(len(data.columns)):
        trait = data.columns[x]
        xticks.append(x)
        ax.violinplot(data.loc[data.index != 'actual', trait], positions=[x])
        xlabels.append(trait.replace("trait_", ""))
    ax.scatter(xticks, data.loc['actual', :])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation="vertical")
    fig.savefig(args.outfile, dpi=100)
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile")
    parser.add_argument("-o", "--outfile")
    parser.add_argument("--debug", default=False, action="store_true")
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    main()