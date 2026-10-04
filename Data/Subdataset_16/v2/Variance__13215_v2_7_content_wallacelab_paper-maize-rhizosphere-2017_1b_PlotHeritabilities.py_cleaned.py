import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def fonk1():
    b1 = fonk2()
    print(f"Plotting heritabilities from {b1.infile}")
    b2 = pd.read_csv(b1.infile, sep='\t')
    b3 = np.argsort(b2.loc['actual', :])[::-1]
    b2 = b2.iloc[:, b3]
    fig, b4 = plt.subplots(figsize=(5 + 0.25 * len(b2.columns), 5))
    b4.set_title("Distributions of null heritabilities")
    b4.set_xlabel("Trait")
    b4.set_ylabel("Heritability")
    b5 = b2.index != "actual"
    xticks, b6 = [], []
    for x, trait in enumerate(b2.columns):
        xticks.append(x)
        b4.violinplot(b2.loc[b5, trait], b7 = [x])
        b6.append(trait.replace("trait_", ""))
    b4.scatter(xticks, b2.loc['actual', :], b8 = 'red')
    b4.set_xticks(xticks)
    b4.set_xticklabels(b6, b9 = "vertical")
    fig.savefig(b1.outfile, b10 = 100)
def fonk2():
    b11 = argparse.ArgumentParser(description="Plot heritabilities from a given input file.")
    b11.add_argument("-i", "--infile", b12 = True, help="Input file containing heritabilities.")
    b11.add_argument("-o", "--outfile", b12 = True, help="Output file to save the plot.")
    b11.add_argument("--debug", b13 = False, action="store_true", help="Enable debug mode.")
    return b11.fonk2()
if b14 = = '__main__':
    fonk1()