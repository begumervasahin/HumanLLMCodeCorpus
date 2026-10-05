import os
import sys
import argparse
import pickle
import logging
import numpy as np
from model import MultitaskLSTM
from data import prepare_dataset, load_dataset
np.random.seed(10)
logging.basicConfig(level=logging.INFO, format='%(message)s')
def parse_arguments():
    parser = argparse.ArgumentParser(description='Train Multitask LSTM Model')
    parser.add_argument('--model_name', default='', help='Name of the model', type=str)
    parser.add_argument('--nb_epochs', default=50, help='Number of epochs', type=int)
    parser.add_argument('--early_stopping', default=5, help='Early stopping criteria', type=int)
    parser.add_argument('--batch_size', default=20, help='Batch size for training', type=int)
    parser.add_argument('--optimizer', default='adam', help='Optimizer for training', type=str)
    parser.add_argument('--classifier', default='softmax', help='Classifier type', type=str)
    parser.add_argument('--loss', default='categorical_crossentropy', help='Loss function', type=str)
    parser.add_argument('--dump_prefix', default='models/', help='Prefix for model dump name', type=str)
    parser.add_argument('--lstm', default=3, help='Number of LSTM layers', type=int)
    parser.add_argument('--lstm_size', default=160, help='Size of LSTM layers', type=int)
    parser.add_argument('--dropout', default=0.25, help='Dropout rate', type=float)
    return parser.parse_args()
def main():
    args = parse_arguments()
    dump_path = '{}{}'.format(args.dump_prefix, args.model_name)
    model_params = {
        'classifier': args.classifier,
        'optimizer': args.optimizer,
        'dropout': args.dropout,
        'lstm_units': args.lstm_size,
        'early_stopping': args.early_stopping,
        'batch_size': args.batch_size,
        'lstm_size': [args.lstm_size] * args.lstm,
        'lemmatization': True,
        'char_embeddings': 'lstm',
        'char_maxlen': 100,
        'model_path': dump_path,
    }
    name = args.model_name
    labels = ['POS']
    columns = {1: 'tokens', 3: 'POS'}
    morph_features = {
        5: 'abbr', 6: 'animacy', 7: 'aspect', 8: 'case', 9: 'definite',
        10: 'degree', 11: 'evident', 12: 'foreign', 13: 'gender',
        14: 'mood', 15: 'numtype', 16: 'number', 17: 'person',
        18: 'polarity', 19: 'polite', 20: 'poss', 21: 'prontype',
        22: 'reflex', 23: 'tense', 24: 'verbform', 25: 'voice',
    }
    columns.update(morph_features)
    labels += morph_features.values()
    if model_params['lemmatization'] and model_params['char_embeddings']:
        columns.update({2: 'lemma'})
    data = (name, columns)
    embeddings_path = f'wordvec/{name}.vec'
    characters_path = f'characters/{name}.chars'
    pickle_dump = prepare_dataset(embeddings_path, data, characters_path)
    embeddings, _, dataset = load_dataset(pickle_dump)
    mappings = dataset['mappings']
    model = MultitaskLSTM(name, embeddings, (dataset, labels,), params=model_params)
    if not os.path.isdir(dump_path):
        os.mkdir(dump_path)
    model.train(args.nb_epochs)
    mappings_dump = {
        'mappings': mappings,
        'char_len': model.char_len
    }
    with open(f'mappings/{name}_mappings.pkl', 'wb') as output:
        pickle.dump(mappings_dump, output)
if __name__ == "__main__":
    main()