import pandas as pd
import json
def fonk1(b5, b7, label):
    b1 = b5[b5[label] == 0][b7]
    b2 = b5[b5[label] == 1][b7]
    b3 = {}
    for class_label, class_data in zip([0, 1], [b1, b2]):
        b3[class_label] = class_data.describe().loc[['mean', 'std']].to_dict()
    return b3
def fonk2(b4 = 'train-data.csv', output_file='b3.json', label='RainToday'):
    b5 = pd.read_csv(b4)
    b5.set_index('Date', b6 = True)
    b7 = list(b5.select_dtypes(include='float64'))
    b3 = fonk1(b5, b7, label)
    with open(output_file, 'w+') as out_file:
        json.dump(b3, out_file)
if b8 = = '__main__':
    import argparse
    b9 = argparse.ArgumentParser()
    b9.add_argument('-i', '--b4', b10 = 'train-data.csv', dest='b4', help="input file for training [b10 : %(b10)s]")
    b9.add_argument('-o', '--output_file', b10 = 'b3.json', dest='output_file', help="output b3 file [b10 : %(b10)s]")
    b9.add_argument('-l', '--target_label', b10 = 'RainToday', dest='label', help="target label [b10 : %(b10)s]")
    b11 = b9.parse_args()
    fonk2(b11.b4, b11.output_file, b11.label)