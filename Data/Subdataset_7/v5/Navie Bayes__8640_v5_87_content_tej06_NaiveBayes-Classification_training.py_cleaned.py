import pandas as pd
import json
def fonk1(b9, b11, label):
    b1 = b9[b9[label] == 0][b11]
    b2 = b9[b9[label] == 1][b11]
    b3 = dict(b1.mean(axis=0))
    b4 = dict(b1.std(axis=0))
    b5 = dict(b2.mean(axis=0))
    b6 = dict(b2.std(axis=0))
    b7 = {0: {}, 1: {}}
    for feat in b11:
        b7[0][feat] = [b3[feat], b4[feat]]
        b7[1][feat] = [b5[feat], b6[feat]]
    return b7
def fonk2(b8 = 'train-data.csv', output_file='b7.json', label='RainToday'):
    b9 = pd.read_csv(b8)
    b9.set_index('Date', b10 = True)
    b11 = list(b9.select_dtypes(include='float64'))
    b7 = fonk1(b9, b11, label)
    with open(output_file, 'w+') as out_file:
        json.dump(b7, out_file)
if b12 = = '__main__':
    import argparse
    b13 = argparse.ArgumentParser()
    b13.add_argument('-i', '--b8', b14 = 'train-data.csv', dest='b8', help="input file for training [b14: %(b14)s]")
    b13.add_argument('-o', '--output_file', b14 = 'b7.json', dest='output_file', help="output b7 file [b14: %(b14)s]")
    b13.add_argument('-l', '--target_label', b14 = 'RainToday', dest='label', help="target label [b14: %(b14)s]")
    b15 = b13.parse_args()
    fonk2(b15.b8, b15.output_file, b15.label)