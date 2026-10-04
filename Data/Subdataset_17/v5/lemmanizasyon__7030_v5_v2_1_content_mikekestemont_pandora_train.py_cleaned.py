from __future__ import print_function
import sys
import pandora.utils
from pandora.tagger import Tagger
def load_data(directory, config_params):
    return pandora.utils.load_annotated_dir(
        directory=directory,
        format='tab',
        extension='.tsv',
        include_pos=config_params['include_pos'],
        include_lemma=config_params['include_lemma'],
        include_morph=config_params['include_morph'],
        nb_instances=None
    )
def train_tagger(config_path):
    print('::: Training Started :::')
    config_params = pandora.utils.get_param_dict(config_path)
    config_params['config_path'] = config_path
    train_data = load_data('data/medieval_latin/train', config_params)
    dev_data = load_data('data/medieval_latin/test', config_params)
    tagger = Tagger(**config_params)
    tagger.setup_to_train(train_data=train_data, dev_data=dev_data)
    num_epochs = int(config_params['nb_epochs'])
    for epoch in range(num_epochs):
        tagger.epoch()
        tagger.save()
    tagger.save()
    print('::: Training Ended :::')
def main():
    if len(sys.argv) != 2:
        print('Usage: python script.py <config_file_path>')
        sys.exit(1)
    config_file_path = sys.argv[1]
    train_tagger(config_file_path)
if __name__ == '__main__':
    main()