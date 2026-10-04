import argparse
import matplotlib.pyplot as plt
import pandas as pd
def fonk1():
    b1 = argparse.ArgumentParser(description='Plot b10 from a given file.')
    b1.add_argument('b10', b2 = str, help='Specify the path of b10.txt')
    b1.add_argument('--b4', b2 = str, default=None, help='Title of the plot')
    return b1.parse_args()
def fonk2(file_path):
    return pd.read_csv(file_path, b3 = '\t')
def fonk3(b10, b4 = None):
    plt.figure(b5 = (10, 6))
    for col in ['mean', 'median']:
        plt.plot(b10['steps'], b10[col], b6 = col)
    if b4:
        plt.b4(b4)
    plt.xlabel('Steps')
    plt.ylabel('Score')
    plt.legend(b7 = 'best')
def fonk4(file_path):
    b8 = f"{file_path}.png"
    plt.savefig(b8)
    print(f'Saved the figure as {b8}')
def fonk5():
    b9 = fonk1()
    b10 = fonk2(b9.b10)
    fonk3(b10, b9.b4)
    fonk4(b9.b10)
if b11 = = '__main__':
    fonk5()