from __future__ import print_function
import sys
import pandora.utils
from pandora.tagger import Tagger
import os, codecs
def main(cf_path):
    print('::: started :::')
    params = pandora.utils.get_param_dict(cf_path)
    params['config_path'] = cf_path
    train_data = pandora.utils.load_annotated_dir(
        'data/medieval_latin/train',
        format='tab',
        extension='.tsv',
        include_pos=params['include_pos'],
        include_lemma=params['include_lemma'],
        include_morph=params['include_morph'],
        nb_instances=None
    )
    dev_data = pandora.utils.load_annotated_dir(
        'data/medieval_latin/test',
        format='tab',
        extension='.tsv',
        include_pos=params['include_pos'],
        include_lemma=params['include_lemma'],
        include_morph=params['include_morph'],
        nb_instances=None
    )
    tagger = Tagger(**params)
    tagger.setup_to_train(train_data=train_data, dev_data=dev_data)
    for i in range(int(params['nb_epochs'])):
        tagger.epoch()
        tagger.save()
    tagger.save()
    print('::: ended :::')
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_path>")
    else:
        main(sys.argv[1])