import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1():
    b1 = fonk2()
    print("Plotting heritabilities from", b1.infile)
    b2 = pd.read_csv(b1.infile, sep='\t')
    b3 = fonk3(b2)
    b2 = b2.iloc[:, b3]
    fonk4(b2, b1.outfile)
def fonk2():
    b4 = argparse.ArgumentParser()
    b4.add_argument("-i", "--infile", b5 = "Input file containing heritability b2")
    b4.add_argument("-o", "--outfile", b5 = "Output file to save the plot")
    b4.add_argument("--debug", b6 = False, action="store_true")
    return b4.parse_args()
def fonk3(b2):
    return np.argsort(b2.loc['actual', :])[::-1]
def fonk4(b2, outfile):
    b7 = plt.figure(figsize=(fonk5(b2), 5))
    b8 = gridspec.GridSpec(nrows=100, ncols=100)
    b9 = b7.add_subplot(b8[:80, :], title="Distributions of null heritabilities", xlabel="Trait", ylabel="Heritability")
    xticks, b10 = [], []
    for x, trait in enumerate(b2.columns):
        xticks.append(x)
        b9.violinplot(b2.loc[b2.index != 'actual', trait], b11 = [x])
        b10.append(trait.replace("trait_", ""))
    b9.scatter(xticks, b2.loc['actual', :])
    b9.set_xticks(xticks)
    b9.set_xticklabels(b10, b12 = "vertical")
    b7.savefig(outfile, b13 = 100)
def fonk5(b2):
    return 5 + .25 * len(b2.columns)
if b14 = = '__main__':
    fonk1()