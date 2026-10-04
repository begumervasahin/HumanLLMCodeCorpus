import argparse
import matplotlib.pyplot as plt
import pandas as pd
def fonk1():
    b1 = argparse.ArgumentParser(description='Plot b9 from a given file.')
    b1.add_argument('b9', b2 = str, help='Specify the path of b9.txt')
    b1.add_argument('--b4', b2 = str, default=None, help='Title of the plot')
    return b1.parse_args()
def fonk2(file_path):
    return pd.read_csv(file_path, b3 = '\t')
def fonk3(b9, b4 = None):
    for col in ['mean', 'median']:
        plt.plot(b9['steps'], b9[col], b5 = col)
    if b4 is not None:
        plt.b4(b4)
    plt.xlabel('Steps')
    plt.ylabel('Score')
    plt.legend(b6 = 'best')
def fonk4(file_path):
    b7 = file_path + '.png'
    plt.savefig(b7)
    print(f'Saved a figure as {b7}')
def fonk5():
    b8 = fonk1()
    b9 = fonk2(b8.b9)
    fonk3(b9, b8.b4)
    fonk4(b8.b9)
if b10 = = '__main__':
    fonk5()