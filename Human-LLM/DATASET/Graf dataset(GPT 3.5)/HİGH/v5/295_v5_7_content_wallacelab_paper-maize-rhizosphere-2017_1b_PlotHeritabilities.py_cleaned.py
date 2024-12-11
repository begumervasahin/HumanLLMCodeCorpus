import argparse
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
b1 = False
def fonk1():
    b2 = fonk6()
    print("Plotting heritabilities from", b2.infile)
    b3 = pd.read_csv(b2.infile, sep='\t')
    b3 = fonk2(b3)
    b7, b4 = fonk3(b3)
    fonk4(b4, b3)
    fonk5(b7, b2.outfile)
def fonk2(b3):
    b5 = np.argsort(b3.loc['actual', :])[::-1]
    return b3.iloc[:, b5]
def fonk3(b3):
    b6 = 5 + .25 * len(b3.columns)
    a1 = 5
    b7 = plt.figure(figsize=(b6, a1))
    b8 = gridspec.GridSpec(nrows=100, ncols=100)
    b4 = b7.add_subplot(b8[:80, :], title="Distributions of null heritabilities", xlabel="trait", ylabel="Heritability")
    return b7, b4
def fonk4(b4, b3):
    b9 = b3.index != "actual"
    xticks, b10 = [], []
    for x, trait in enumerate(b3.columns):
        xticks.append(x)
        b4.violinplot(b3.loc[b9, trait], b11 = [x])
        b10.append(trait.replace("trait_", ""))
    b4.scatter(xticks, b3.loc['actual', :])
    b4.set_xticks(xticks)
    b4.set_xticklabels(b10, b12 = "vertical")
def fonk5(b7, outfile):
    b7.savefig(outfile, b13 = 100)
def fonk6():
    b14 = argparse.ArgumentParser()
    b14.add_argument("-i", "--infile", b15 = "Input file")
    b14.add_argument("-o", "--outfile", b15 = "Output file")
    b14.add_argument("--b1", b16 = False, action="store_true", b15="Enable debugging")
    b2 = b14.fonk6()
    global b1
    b1 = b2.b1
    return b2
if b17 = = '__main__':
    fonk1()