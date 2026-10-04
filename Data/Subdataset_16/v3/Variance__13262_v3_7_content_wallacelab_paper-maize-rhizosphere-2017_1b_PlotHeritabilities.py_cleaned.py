import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1():
    b1 = fonk2()
    print(f"Plotting heritabilities from {b1.infile}")
    b2 = fonk3(b1.infile)
    fonk4(b2, b1.outfile)
def fonk2():
    b3 = argparse.ArgumentParser(description="Plot heritabilities from a given input file.")
    b3.add_argument("-i", "--infile", b4 = True, help="Input file containing heritabilities.")
    b3.add_argument("-o", "--outfile", b4 = True, help="Output file to save the plot.")
    b3.add_argument("--debug", b5 = False, action="store_true", help="Enable debug mode.")
    return b3.fonk2()
def fonk3(infile):
    b2 = pd.read_csv(infile, sep='\t')
    b6 = np.argsort(b2.loc['actual', :])[::-1]
    return b2.iloc[:, b6]
def fonk4(b2, outfile):
    fig, b7 = plt.subplots(figsize=(5 + 0.25 * len(b2.columns), 5))
    b7.set_title("Distributions of null heritabilities")
    b7.set_xlabel("Trait")
    b7.set_ylabel("Heritability")
    b8 = b2.index != "actual"
    xticks, b9 = [], []
    for x, trait in enumerate(b2.columns):
        xticks.append(x)
        b7.violinplot(b2.loc[b8, trait], b10 = [x])
        b9.append(trait.replace("trait_", ""))
    b7.scatter(xticks, b2.loc['actual', :], b11 = 'red')
    b7.set_xticks(xticks)
    b7.set_xticklabels(b9, b12 = "vertical")
    fig.savefig(outfile, b13 = 100)
if b14 = = '__main__':
    fonk1()