from __future__ import print_function
import sys
import pandora.utils
from pandora.tagger import Tagger
def load_configuration(config_path):
    params = pandora.utils.get_param_dict(config_path)
    params['config_path'] = config_path
    return params
def load_data(data_dir, params):
    return pandora.utils.load_annotated_dir(
        data_dir,
        format='tab',
        extension='.tsv',
        include_pos=params['include_pos'],
        include_lemma=params['include_lemma'],
        include_morph=params['include_morph'],
        nb_instances=None
    )
def train_tagger(config_path):
    print('::: Training Started :::')
    params = load_configuration(config_path)
    train_data = load_data('data/medieval_latin/train', params)
    dev_data = load_data('data/medieval_latin/test', params)
    tagger = Tagger(**params)
    tagger.setup_to_train(train_data=train_data, dev_data=dev_data)
    for epoch in range(int(params['nb_epochs'])):
        tagger.epoch()
        tagger.save()
    tagger.save()
    print('::: Training Ended :::')
def main():
    if len(sys.argv) != 2:
        print('Usage: python script.py <config_file_path>')
        sys.exit(1)
    config_path = sys.argv[1]
    train_tagger(config_path)
if __name__ == '__main__':
    main()