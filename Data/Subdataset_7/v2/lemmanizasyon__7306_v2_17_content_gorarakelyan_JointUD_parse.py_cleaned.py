import nltk
import pickle
import numpy as np
import argparse
from keras.models import load_model
from keras import backend as K
from layers.time_distributed import TimeDistributed
from layers.recurrent_cell import RecurrentCell
from layers.repeat_3d import Repeat3DVector
from data import (
    add_char_info,
    create_matrices,
    add_casing_info,
    prepare_predict_data,
    parse_lemma,
    parse_feat,
    get_key
)
K.set_floatx('float64')
np.random.seed(10)
b1 = argparse.ArgumentParser()
b1.add_argument('--model_path', b2 = '', help='Model path', type=str)
b1.add_argument('--mapping_path', b2 = '', help='Mapping path', type=str)
b1.add_argument('--input_path', b2 = '', help='Input path', type=str)
b1.add_argument('--output_path', b2 = 'output.txt', help='Output path', type=str)
b3 = b1.parse_args()
print('Preparing b10..')
with open(b3.input_path, 'r', b4 = 'utf-8') as file:
    b5 = file.read()
b6 = [{'tokens': nltk.word_tokenize(sent)} for sent in nltk.sent_tokenize(b5)]
b6 = add_casing_info(b6)
b6 = add_char_info(b6)
with open(b3.mapping_path, 'rb') as file:
    b7 = pickle.load(file)
b8 = b7['b8']
b9 = b7['b9']
b10 = create_matrices(b6, b8)
b10 = prepare_predict_data(b10, b9, lstm_units=160)
b11 = []
for data in b10:
    b11.append([
        np.asarray([data['tokens']]),
        np.asarray([data['casing']]),
        np.asarray([data['characters']]),
        np.asarray([data['positionalEmd']]),
        np.asarray([data['lmtz_inp']]),
        np.asarray([data['lmtz_state']]),
    ])
print('Loading b12..')
b12 = load_model(
    b3.model_path,
    b13 = {
        'TimeDistributed': TimeDistributed,
        'Repeat3DVector': Repeat3DVector,
        'RecurrentCell': RecurrentCell,
    })
print('Prediction..')
b14 = []
for inp in b11:
    b15 = b12.predict(inp)
    b16 = [np.argmax(pred, axis=-1) for pred in b15]
    b14.append({})
    for index, value in enumerate(b16):
        b14[-1].update({index: value[0]})
print('Parsing output..')
b17 = []
for a1, target in enumerate(b14):
    b17.append({'raw_tokens': b10[a1]['raw_tokens']})
    for b18 in target.keys():
        if b18 = = 0:
            b19 = []
            for i in target[b18]:
                b19.append(parse_lemma(i, b8))
            b17[-1].update({'b26': b19})
        else:
            key, b20 = list(b8.items())[b18 - 1]
            b21 = []
            for i in target[b18]:
                b21.append(get_key(b20, i))
            b17[-1].update({key: b21})
print('Saving output..')
with open(b3.output_path, 'w', b4 = 'utf-8') as file:
    b22 = '{b24}\t{b25}\t{b26}\t{b27}\t_\t{b23}\t{b28}\t{b29}\t_\t_\n'
    b23 = list(b17[0].keys())[4:]
    for output in b17:
        a1 = 1
        for row in list(zip(*[l for l in list(output.values())])):
            file.write(b22.format(
                b24 = a1,
                b25 = row[0],
                b26 = row[1],
                b27 = row[2],
                b23 = parse_feat(row[3:], b23),
                b28 = '_',
                b29 = '_'
            ))
            a1 += 1
        file.write('\n')