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
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def load_mappings(mapping_path):
    with open(mapping_path, 'rb') as file:
        return pickle.load(file)
def prepare_input_data(dataset):
    input_data = []
    for data in dataset:
        input_data.append([
            np.asarray([data['tokens']]),
            np.asarray([data['casing']]),
            np.asarray([data['characters']]),
            np.asarray([data['positionalEmd']]),
            np.asarray([data['lmtz_inp']]),
            np.asarray([data['lmtz_state']]),
        ])
    return input_data
def predict_labels(model, input_data):
    targets = []
    for inp in input_data:
        predictions = model.predict(inp)
        predicted_labels = [np.argmax(pred, axis=-1) for pred in predictions]
        targets.append({})
        for index, value in enumerate(predicted_labels):
            targets[-1].update({index: value[0]})
    return targets
def parse_output(targets, dataset, mappings):
    parsed_output = []
    for idx, target in enumerate(targets):
        parsed_output.append({'raw_tokens': dataset[idx]['raw_tokens']})
        for label in target.keys():
            if label == 0:
                lemmas = [parse_lemma(i, mappings) for i in target[label]]
                parsed_output[-1].update({'lemma': lemmas})
            else:
                key, val = list(mappings.items())[label - 1]
                label_values = [get_key(val, i) for i in target[label]]
                parsed_output[-1].update({key: label_values})
    return parsed_output
def save_output(parsed_output, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        template = '{id}\t{token}\t{lemma}\t{pos}\t_\t{features}\t{head}\t{dep}\t_\t_\n'
        features = list(parsed_output[0].keys())[4:]
        for output in parsed_output:
            idx = 1
            for row in zip(*[l for l in list(output.values())]):
                file.write(template.format(
                    id=idx,
                    token=row[0],
                    lemma=row[1],
                    pos=row[2],
                    features=parse_feat(row[3:], features),
                    head='_',
                    dep='_'
                ))
                idx += 1
            file.write('\n')
def main(args):
    print('Preparing dataset..')
    text = load_text(args.input_path)
    sentences = [{'tokens': nltk.word_tokenize(sent)} for sent in nltk.sent_tokenize(text)]
    sentences = add_casing_info(sentences)
    sentences = add_char_info(sentences)
    mapping_info = load_mappings(args.mapping_path)
    mappings = mapping_info['mappings']
    char_len = mapping_info['char_len']
    dataset = create_matrices(sentences, mappings)
    dataset = prepare_predict_data(dataset, char_len, lstm_units=160)
    nn_input = prepare_input_data(dataset)
    print('Loading model..')
    model = load_model(
        args.model_path,
        custom_objects={
            'TimeDistributed': TimeDistributed,
            'Repeat3DVector': Repeat3DVector,
            'RecurrentCell': RecurrentCell,
        })
    print('Prediction..')
    targets = predict_labels(model, nn_input)
    print('Parsing output..')
    parsed_output = parse_output(targets, dataset, mappings)
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