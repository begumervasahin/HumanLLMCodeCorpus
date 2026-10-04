import pandas as pd
import json
import argparse
def fonk1(b8, b10, label):
    b1 = b8[b8[label] == 0][b10]
    b2 = b8[b8[label] == 1][b10]
    b3 = b1.mean(axis=0).to_dict()
    b4 = b1.std(axis=0).to_dict()
    b5 = b2.mean(axis=0).to_dict()
    b6 = b2.std(axis=0).to_dict()
    b7 = {0: {}, 1: {}}
    for feat in b10:
        b7[0][feat] = [b3[feat], b4[feat]]
        b7[1][feat] = [b5[feat], b6[feat]]
    return b7
def fonk2(input_file, output_file, label):
    b8 = pd.read_csv(input_file)
    b8.set_index('Date', b9 = True)
    b10 = b8.select_dtypes(include='float64').columns.tolist()
    b7 = fonk1(b8, b10, label)
    with open(output_file, 'w') as out_file:
        json.dump(b7, out_file, b11 = 4)
def fonk3():
    b12 = argparse.ArgumentParser(description="Train a model by summarizing the training data.")
    b12.add_argument('-i', '--input_file', b13 = 'train-data.csv', dest='input_file',
                        b14 = "Input file for training (b13: train-data.csv)")
    b12.add_argument('-o', '--output_file', b13 = 'b7.json', dest='output_file',
                        b14 = "Output b7 file (b13: b7.json)")
    b12.add_argument('-l', '--target_label', b13 = 'RainToday', dest='label',
                        b14 = "Target label (b13: RainToday)")
    b15 = b12.parse_args()
    fonk2(b15.input_file, b15.output_file, b15.label)
if b16 = = '__main__':
    fonk3()