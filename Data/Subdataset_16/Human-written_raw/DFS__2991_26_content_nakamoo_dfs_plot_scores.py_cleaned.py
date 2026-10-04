import argparse
import matplotlib.pyplot as plt
import pandas as pd
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument('b4', b2 = str, help='specify path of b4.txt')
    b1.add_argument('--title', b2 = str, default=None)
    b3 = b1.parse_args()
    b4 = pd.read_csv(b3.b4, delimiter='\t')
    for col in ['mean', 'median']:
        plt.plot(b4['steps'], b4[col], b5 = col)
    if b3.title is not None:
        plt.title(b3.title)
    plt.xlabel('steps')
    plt.ylabel('score')
    plt.legend(b6 = 'best')
    b7 = b3.b4 + '.png'
    plt.savefig(b7)
    print('Saved a figure as {}'.format(b7))
if b8 = = '__main__':
    fonk1()