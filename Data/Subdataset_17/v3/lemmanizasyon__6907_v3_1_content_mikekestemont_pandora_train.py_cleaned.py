from __future__ import print_function
import sys
import pandora.utils
from pandora.tagger import Tagger
def load_data(directory, params):
    return pandora.utils.load_annotated_dir(
        directory=directory,
        format='tab',
        extension='.tsv',
        include_pos=params.get('include_pos', False),
        include_lemma=params.get('include_lemma', False),
        include_morph=params.get('include_morph', False),
        nb_instances=None
    )
def train_tagger(params):
    train_data = load_data('data/medieval_latin/train', params)
    dev_data = load_data('data/medieval_latin/test', params)
    tagger = Tagger(**params)
    tagger.setup_to_train(train_data=train_data, dev_data=dev_data)
    num_epochs = int(params.get('nb_epochs', 10))
    for epoch in range(num_epochs):
        tagger.epoch()
        tagger.save()
    tagger.save()
def main(config_path):
    print('::: started :::')
    params = pandora.utils.get_param_dict(config_path)
    params['config_path'] = config_path
    train_tagger(params)
    print('::: ended :::')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_path>")
    else:
        main(sys.argv[1])