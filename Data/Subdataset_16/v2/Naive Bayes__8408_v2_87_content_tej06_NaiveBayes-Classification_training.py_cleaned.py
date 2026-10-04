import pandas as pd
import json
import argparse
def fonk1(b4, b6, label):
    b1 = b4[b4[label] == 0][b6]
    b2 = b4[b4[label] == 1][b6]
    b3 = {
        0: {feat: [b1[feat].mean(), b1[feat].std()] for feat in b6},
        1: {feat: [b2[feat].mean(), b2[feat].std()] for feat in b6}
    }
    return b3
def fonk2(input_file, output_file, label):
    b4 = pd.read_csv(input_file)
    b4.set_index('Date', b5 = True)
    b6 = list(b4.select_dtypes(include='float64').columns)
    b3 = fonk1(b4, b6, label)
    with open(output_file, 'w') as out_file:
        json.dump(b3, out_file, b7 = 4)
if b8 = = '__main__':
    b9 = argparse.ArgumentParser(description="Train a model and save the b3 to a JSON file.")
    b9.add_argument('-i', '--input_file', b10 = 'train-data.csv', dest='input_file',
                        b11 = "Input file for training [b10: %(b10)s]")
    b9.add_argument('-o', '--output_file', b10 = 'b3.json', dest='output_file',
                        b11 = "Output b3 file [b10: %(b10)s]")
    b9.add_argument('-l', '--target_label', b10 = 'RainToday', dest='label',
                        b11 = "Target label [b10: %(b10)s]")
    b12 = b9.parse_args()
    fonk2(b12.input_file, b12.output_file, b12.label)