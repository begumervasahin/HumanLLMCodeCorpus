from __future__ import print_function
import sys
import pandora.utils
from pandora.tagger import Tagger
def load_annotated_data(directory, params, nb_instances=None):
    return pandora.utils.load_annotated_dir(
        directory,
        format='tab',
        extension='.tsv',
        include_pos=params.get('include_pos', False),
        include_lemma=params.get('include_lemma', False),
        include_morph=params.get('include_morph', False),
        nb_instances=nb_instances
    )
def train_tagger(config_path):
    print('::: Training Started :::')
    params = pandora.utils.get_param_dict(config_path)
    params['config_path'] = config_path
    train_data = load_annotated_data('data/medieval_latin/train', params)
    dev_data = load_annotated_data('data/medieval_latin/test', params)
    tagger = Tagger(**params)
    tagger.setup_to_train(train_data=train_data, dev_data=dev_data)
    nb_epochs = int(params['nb_epochs'])
    for epoch in range(nb_epochs):
        print(f'::: Epoch {epoch + 1}/{nb_epochs} :::')
        tagger.epoch()
        tagger.save()
    tagger.save()
    print('::: Training Ended :::')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <config_file_path>')
        sys.exit(1)
    config_path = sys.argv[1]
    train_tagger(config_path)