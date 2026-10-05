import nltk
import pickle
import numpy as np
import argparse
from keras.models import load_model
from keras import backend as K
from layers.time_distributed import TimeDistributed
from layers.recurrent_cell import RecurrentCell
from layers.repeat_3d import Repeat3DVector
from data import add_char_info, create_matrices, add_casing_info, prepare_predict_data, parse_lemma, parse_feat, get_key
K.set_floatx('float64')
np.random.seed(10)
def load_data(input_path, mapping_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = [{'tokens': nltk.word_tokenize(sent)} for sent in nltk.sent_tokenize(text)]
    sentences = add_casing_info(sentences)
    sentences = add_char_info(sentences)
    with open(mapping_path, 'rb') as f:
        info = pickle.load(f)
    mappings = info['mappings']
    char_len = info['char_len']
    dataset = create_matrices(sentences, mappings)
    dataset = prepare_predict_data(dataset, char_len, lstm_units=160)
    return dataset, mappings
def predict_and_parse(model, dataset, mappings):
    parsed_output = []
    for data in dataset:
        nn_input = {
            'tokens': np.asarray([data['tokens']]),
            'casing': np.asarray([data['casing']]),
            'characters': np.asarray([data['characters']]),
            'positionalEmd': np.asarray([data['positionalEmd']]),
            'lmtz_inp': np.asarray([data['lmtz_inp']]),
            'lmtz_state': np.asarray([data['lmtz_state']])
        }
        pred = model.predict(nn_input)
        output = [p.argmax(axis=-1) for p in pred]
        parsed_data = {'raw_tokens': data['raw_tokens']}
        for label in range(len(output)):
            if label == 0:
                lemmas = [parse_lemma(i, mappings) for i in output[label]]
                parsed_data['lemma'] = lemmas
            else:
                key, value = list(mappings.items())[label - 1]
                label_values = [get_key(value, i) for i in output[label]]
                parsed_data[key] = label_values
        parsed_output.append(parsed_data)
    return parsed_output
def save_output(parsed_output, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        tpl = '{id}\t{token}\t{lemma}\t{pos}\t_\t{features}\t{head}\t{dep}\t_\t_\n'
        features = list(parsed_output[0].keys())[4:]
        for idx, parsed_data in enumerate(parsed_output):
            idx = 1
            for row in zip(*parsed_data.values()):
                token, lemma, pos, *other_features = row
                row = tpl.format(
                    id=idx,
                    token=token,
                    lemma=lemma,
                    pos=pos,
                    features=parse_feat(other_features, features),
                    head='_',
                    dep='_')
                f.write(row)
                idx += 1
            f.write('\n')
def main(args):
    print('Preparing dataset..')
    dataset, mappings = load_data(args.input_path, args.mapping_path)
    print('Loading model..')
    model = load_model(
        args.model_path,
        custom_objects={
            'TimeDistributed': TimeDistributed,
            'Repeat3DVector': Repeat3DVector,
            'RecurrentCell': RecurrentCell,
        })
    print('Prediction and parsing..')
    parsed_output = predict_and_parse(model, dataset, mappings)
    print('Saving output..')
    save_output(parsed_output, args.output_path)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', default='', help='Model path', type=str)
    parser.add_argument('--mapping_path', default='', help='Mapping path', type=str)
    parser.add_argument('--input_path', default='', help='Input path', type=str)
    parser.add_argument('--output_path', default='output.txt', help='Output path', type=str)
    args = parser.parse_args()
    main(args)