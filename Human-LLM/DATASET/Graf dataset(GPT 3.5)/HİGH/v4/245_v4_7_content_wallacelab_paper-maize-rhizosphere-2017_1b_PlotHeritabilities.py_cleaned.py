import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
b1 = False
def fonk1():
    b2 = fonk2()
    print("Plotting heritabilities from", b2.infile)
    b3 = pd.read_csv(b2.infile, sep='\t')
    b4 = np.argsort(b3.loc['actual', :])[::-1]
    b3 = b3.iloc[:, b4]
    b5 = plt.figure(figsize=(5 + .25 * len(b3.columns), 5))
    b6 = gridspec.GridSpec(nrows=100, ncols=100)
    b7 = b5.add_subplot(b6[:80, :], title="Distributions of null heritabilities", xlabel="b10", ylabel="Heritability")
    b8 = b3.index != "actual"
    xticks, b9 = list(), list()
    for x in range(len(b3.columns)):
        b10 = b3.columns[x]
        xticks.append(x)
        b7.violinplot(b3.loc[b8, b10], b11 = [x])
        b9.append(b10.replace("trait_", ""))
    b7.scatter(xticks, b3.loc['actual', :])
    b7.set_xticks(xticks)
    b7.set_xticklabels(b9, b12 = "vertical")
    b5.savefig(b2.outfile, b13 = 100)
def fonk2():
    b14 = argparse.ArgumentParser()
    b14.add_argument("-i", "--infile")
    b14.add_argument("-o", "--outfile")
    b14.add_argument("--b1", b15 = False, action="store_true")
    b2 = b14.fonk2()
    global b1
    b1 = b2.b1
    return b14.fonk2()
if b16 = = '__main__':
    fonk1()