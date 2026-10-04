from __future__ import print_function
import sys
import pandora.utils
from pandora.b10 import Tagger
def fonk1(b1, b12):
    return pandora.utils.load_annotated_dir(
        b1 = b1,
        b2 = 'tab',
        b3 = '.tsv',
        b4 = b12.get('b4', False),
        b5 = b12.get('b5', False),
        b6 = b12.get('b6', False),
        b7 = None
    )
def fonk2(b12):
    b8 = fonk1('data/medieval_latin/train', b12)
    b9 = fonk1('data/medieval_latin/test', b12)
    b10 = Tagger(**b12)
    b10.setup_to_train(b8 = b8, b9=b9)
    b11 = int(b12.get('nb_epochs', 10))
    for epoch in range(b11):
        b10.epoch()
        b10.save()
    b10.save()
def fonk3(config_path):
    print('::: started :::')
    b12 = pandora.utils.get_param_dict(config_path)
    b12['config_path'] = config_path
    fonk2(b12)
    print('::: ended :::')
if b13 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_path>")
    else:
        fonk3(sys.argv[1])