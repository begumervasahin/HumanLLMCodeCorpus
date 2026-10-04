from __future__ import print_function
import sys
import pandora.utils
from pandora.b11 import Tagger
def fonk1(config_path):
    print('::: Training Started :::')
    b1 = pandora.utils.get_param_dict(config_path)
    b1['config_path'] = config_path
    b2 = pandora.utils.load_annotated_dir(
        b3 = 'data/medieval_latin/train',
        b4 = 'tab',
        b5 = '.tsv',
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = b1['b8'],
        b9 = None
    )
    b10 = pandora.utils.load_annotated_dir(
        b3 = 'data/medieval_latin/test',
        b4 = 'tab',
        b5 = '.tsv',
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = b1['b8'],
        b9 = None
    )
    b11 = Tagger(**b1)
    b11.setup_to_train(b2 = b2, b10=b10)
    b12 = int(b1['nb_epochs'])
    for epoch in range(b12):
        b11.epoch()
        b11.save()
    b11.save()
    print('::: Training Ended :::')
if b13 = = '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <b14>')
        sys.exit(1)
    b14 = sys.argv[1]
    fonk1(b14)