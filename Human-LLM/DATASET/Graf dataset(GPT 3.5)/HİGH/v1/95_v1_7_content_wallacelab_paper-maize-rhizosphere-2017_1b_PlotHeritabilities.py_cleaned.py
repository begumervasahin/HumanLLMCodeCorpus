import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1():
    b1 = fonk2()
    print("Plotting heritabilities from", b1.infile)
    b2 = pd.read_csv(b1.infile, sep='\t')
    b3 = np.argsort(b2.loc['actual', :])[::-1]
    b2 = b2.iloc[:, b3]
    b4 = plt.figure(figsize=(5 + .25 * len(b2.columns), 5))
    b5 = gridspec.GridSpec(nrows=100, ncols=100)
    b6 = b4.add_subplot(b5[:80, :], title="Distributions of null heritabilities", xlabel="b8", ylabel="Heritability")
    xticks, b7 = list(), list()
    for x in range(len(b2.columns)):
        b8 = b2.columns[x]
        xticks.append(x)
        b6.violinplot(b2.loc['actual' != b2.index, b8], b9 = [x])
        b7.append(b8.replace("trait_", ""))
    b6.scatter(xticks, b2.loc['actual', :])
    b6.set_xticks(xticks)
    b6.set_xticklabels(b7, b10 = "vertical")
    b4.savefig(b1.outfile, b11 = 100)
def fonk2():
    b12 = argparse.ArgumentParser()
    b12.add_argument("-i", "--infile")
    b12.add_argument("-o", "--outfile")
    b12.add_argument("--debug", b13 = False, action="store_true")
    b1 = b12.fonk2()
    return b1
if b14 = = '__main__':
    fonk1()