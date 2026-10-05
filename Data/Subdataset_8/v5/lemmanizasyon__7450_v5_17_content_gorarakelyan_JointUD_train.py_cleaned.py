import os
import sys
import argparse
import pickle
import logging
import numpy as np
from model import MultitaskLSTM
from data import prepare_dataset, load_dataset
np.random.seed(10)
logging_level = logging.INFO
logger = logging.getLogger()
logger.setLevel(logging_level)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging_level)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', default='', help='Model name', type=str)
    parser.add_argument('--nb_epochs', default=50, help='Number of Epochs', type=int)
    parser.add_argument('--early_stopping', default=5, help='Early Stopping', type=int)
    parser.add_argument('--batch_size', default=20, help='Batch Size', type=int)
    parser.add_argument('--optimizer', default='adam', help='Optimizer', type=str)
    parser.add_argument('--classifier', default='softmax', help='Classifier', type=str)
    parser.add_argument('--loss', default='categorical_crossentropy', help='Loss', type=str)
    parser.add_argument('--dump_prefix', default='models/', help='Model dump name prefix', type=str)
    parser.add_argument('--lstm', default=3, type=int)
    parser.add_argument('--lstm_size', default=160, type=int)
    parser.add_argument('--dropout', default=0.25, type=float)
    return parser.parse_args()
def create_model_parameters(args):
    return {
        'classifier': args.classifier,
        'optimizer': args.optimizer,
        'dropout': args.dropout,
        'lstm_units': args.lstm_size,
        'early_stopping': args.early_stopping,
        'batch_size': args.batch_size,
        'lstm_size': [args.lstm_size for _ in range(args.lstm)],
        'lemmatization': True,
        'char_embeddings': 'lstm',
        'char_maxlen': 100,
        'model_path': '{}{}'.format(args.dump_prefix, args.model_name),
    }
def create_label_mappings(args):
    labels = ['POS']
    columns = {
        1: 'tokens',
        3: 'POS',
    }
    morph_features = {
        5: 'abbr', 6: 'animacy', 7: 'aspect', 8: 'case', 9: 'definite',
        10: 'degree', 11: 'evident', 12: 'foreign', 13: 'gender',
        14: 'mood', 15: 'numtype', 16: 'number', 17: 'person',
        18: 'polarity', 19: 'polite', 20: 'poss', 21: 'prontype',
        22: 'reflex', 23: 'tense', 24: 'verbform', 25: 'voice',
    }
    columns.update(morph_features)
    labels += morph_features.values()
    if args.lemmatization and args.char_embeddings:
        columns.update({2: 'lemma'})
    return args.model_name, columns, labels
def main():
    args = parse_arguments()
    model_params = create_model_parameters(args)
    name, columns, labels = create_label_mappings(args)
    data = (name, columns)
    embeddings_path = 'wordvec/' + name + '.vec'
    characters_path = 'characters/' + name + '.chars'
    pickle_dump = prepare_dataset(embeddings_path, data, characters_path)
    embeddings, _, dataset = load_dataset(pickle_dump)
    mappings = dataset['mappings']
    model = MultitaskLSTM(name, embeddings, (dataset, labels,), params=model_params)
    if not os.path.isdir(model_params['model_path']):
        os.mkdir(model_params['model_path'])
    model.train(args.nb_epochs)
    mappings_dump = {
        'mappings': mappings,
        'char_len': model.char_len
    }
    with open('mappings/{}_mappings.pkl'.format(name), 'wb') as output:
        pickle.dump(mappings_dump, output)
if __name__ == "__main__":
    main()