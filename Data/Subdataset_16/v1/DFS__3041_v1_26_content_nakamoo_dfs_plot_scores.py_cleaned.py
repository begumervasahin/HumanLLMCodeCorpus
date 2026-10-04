import argparse
import matplotlib.pyplot as plt
import pandas as pd
def fonk1():
    b1 = argparse.ArgumentParser(description='Plot b4 from a given file.')
    b1.add_argument('b4', b2 = str, help='Specify the path of b4.txt')
    b1.add_argument('--title', b2 = str, default=None, help='Title of the plot')
    b3 = b1.parse_args()
    b4 = pd.read_csv(b3.b4, delimiter='\t')
    for col in ['mean', 'median']:
        plt.plot(b4['steps'], b4[col], b5 = col)
    if b3.title is not None:
        plt.title(b3.title)
    plt.xlabel('Steps')
    plt.ylabel('Score')
    plt.legend(b6 = 'best')
    b7 = b3.b4 + '.png'
    plt.savefig(b7)
    print(f'Saved a figure as {b7}')
if b8 = = '__main__':
    fonk1()