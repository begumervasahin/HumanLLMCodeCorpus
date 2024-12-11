b1 = 'jgwall'
import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
b2 = False
def fonk1():
    b3 = fonk2()
    print("Plotting heritabilities from",b3.infile)
    b4 = pd.read_csv(b3.infile, sep='\t')
    b5 = np.argsort(b4.loc['actual',:])[::-1]
    b4 = b4.iloc[:,b5]
    b6 = plt.figure(figsize=(5 + .25 * len(b4.columns), 5))
    b7 = gridspec.GridSpec(nrows=100, ncols=100)
    b8 = b6.add_subplot(b7[:80,:], title="Distributions of null heritabilities", xlabel="b11", ylabel="Heritability")
    b9 = b4.index != "actual"
    xticks, b10 = list(), list()
    for x in range(len(b4.columns)):
        b11 = b4.columns[x]
        xticks.append(x)
        b8.violinplot(b4.loc[b9, b11], b12 = [x])
        b10.append(b11.replace("trait_", ""))
    b8.scatter(xticks, b4.loc['actual',:])
    b8.set_xticks(xticks)
    b8.set_xticklabels(b10, b13 = "vertical")
    b6.savefig(b3.outfile, b14 = 100)
def fonk2():
    b15 = argparse.ArgumentParser()
    b15.add_argument("-i", "--infile")
    b15.add_argument("-o", "--outfile")
    b15.add_argument("--b2", b16 = False, action="store_true")
    b3 = b15.fonk2()
    global b2
    b2 = b3.b2
    return b15.fonk2()
if b17 = = '__main__': fonk1()