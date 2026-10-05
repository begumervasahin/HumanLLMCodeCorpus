from __future__ import print_function
import sys
import pandora.utils
from pandora.b10 import Tagger
def fonk1(b12):
    print('::: Training Started :::')
    b1 = pandora.utils.get_param_dict(b12)
    b1['b12'] = b12
    b2 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/train',
        b3 = 'tab',
        b4 = '.tsv',
        b5 = b1['b5'],
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = None
    )
    b9 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/test',
        b3 = 'tab',
        b4 = '.tsv',
        b5 = b1['b5'],
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = None
    )
    b10 = Tagger(**b1)
    b10.setup_to_train(b2 = b2, b9=b9)
    for epoch in range(int(b1['nb_epochs'])):
        b10.epoch()
        b10.save()
    b10.save()
    print('::: Training Ended :::')
if b11 = = '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <config_file_path>')
        sys.exit(1)
    b12 = sys.argv[1]
    fonk1(b12)