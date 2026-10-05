from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: started :::')
    tagger = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded, now annotating...')
    orig_path = 'data/limborch/orig/'
    new_path = 'data/limborch/tagged/'
    for filename in os.listdir(orig_path):
        if not filename.endswith('.txt'):
            continue
        print('\t +', filename)
        unseen_tokens = pandora.utils.load_unannotated_file(orig_path + filename,
                                                            nb_instances=None,
                                                            tokenized_input=False)
        annotations = tagger.annotate(unseen_tokens)
        output_file_path = new_path + filename
        write_annotations_to_file(output_file_path, annotations)
    print('::: ended :::')
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as f:
        for t, l, p in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            f.write('\t'.join((t.lower(), l.lower(), p.lower())) + '\n')
if __name__ == '__main__':
    main()