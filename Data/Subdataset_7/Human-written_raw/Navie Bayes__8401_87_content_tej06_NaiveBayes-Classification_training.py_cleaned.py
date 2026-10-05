import pandas as pd
import json
def fonk1(b8, b10, label):
	b1 = b8[b8[label]==0][b10]
	b2 = b8[b8[label]==1][b10]
	b3 = dict(b1.mean(axis=0))
	b4 = dict(b1.std(axis=0))
	b5 = dict(b2.mean(axis=0))
	b6 = dict(b2.std(axis=0))
	b7 = {}
	b7[0] = {}
	b7[1] = {}
	for feat in b10:
		b7[0][feat] = [b3[feat], b4[feat]]
		b7[1][feat] = [b5[feat], b6[feat]]
	return b7
def fonk2(input_file, output_file, label):
	b8 = pd.read_csv(input_file)
	b8.set_index('Date', b9 = True)
	b10 = list(b8.select_dtypes(include='float64'))
	b7 = fonk1(b8, b10, label)
	with open(output_file, 'w+') as out_file:
		json.dump(b7, out_file)
if b11 = ='__main__':
	import argparse
	b12 = argparse.ArgumentParser()
	b12.add_argument('-i', '--input_file', b13 = 'train-data.csv', dest='input_file', help=)
	b12.add_argument('-o', '--output_file', b13 = 'b7.json', dest='output_file', help=)
	b12.add_argument('-l', '--target_label', b13 = 'RainToday', dest='label', help=)
	b14 = b12.parse_args()
	fonk2(b14.input_file, b14.output_file, b14.label)