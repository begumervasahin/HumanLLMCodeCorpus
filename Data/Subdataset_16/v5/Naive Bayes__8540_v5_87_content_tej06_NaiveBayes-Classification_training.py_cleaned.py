import pandas as pd
import json
import argparse
def fonk1(b4, b6, label):
    b1 = b4[b4[label] == 0][b6]
    b2 = b4[b4[label] == 1][b6]
    b3 = {0: {}, 1: {}}
    for feat in b6:
        b3[0][feat] = [b1[feat].mean(), b1[feat].std()]
        b3[1][feat] = [b2[feat].mean(), b2[feat].std()]
    return b3
def fonk2(input_file, output_file, label):
    b4 = pd.read_csv(input_file)
    b4.set_index('Date', b5 = True)
    b6 = b4.select_dtypes(include='float64').columns.tolist()
    b3 = fonk1(b4, b6, label)
    with open(output_file, 'w') as out_file:
        json.dump(b3, out_file, b7 = 4)
def fonk3():
    b8 = argparse.ArgumentParser(description="Train a model by summarizing the training data.")
    b8.add_argument('-i', '--input_file', b9 = 'train-data.csv', dest='input_file',
                        b10 = "Input file for training (b9: train-data.csv)")
    b8.add_argument('-o', '--output_file', b9 = 'b3.json', dest='output_file',
                        b10 = "Output b3 file (b9: b3.json)")
    b8.add_argument('-l', '--target_label', b9 = 'RainToday', dest='label',
                        b10 = "Target label (b9: RainToday)")
    b11 = b8.parse_args()
    fonk2(b11.input_file, b11.output_file, b11.label)
if b12 = = '__main__':
    fonk3()