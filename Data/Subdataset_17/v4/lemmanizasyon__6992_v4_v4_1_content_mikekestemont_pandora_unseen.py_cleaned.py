from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: Annotation Process Started :::')
    tagger = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded. Now, annotating...')
    orig_path = 'data/limborch/orig/'
    new_path = 'data/limborch/tagged/'
    for filename in os.listdir(orig_path):
        if filename.endswith('.txt'):
            print(f'\t + Annotating {filename}')
            annotate_file(tagger, orig_path, new_path, filename)
    print('::: Annotation Process Ended :::')
def annotate_file(tagger, orig_path, new_path, filename):
    input_file_path = os.path.join(orig_path, filename)
    unseen_tokens = pandora.utils.load_unannotated_file(
        input_file_path,
        nb_instances=None,
        tokenized_input=False
    )
    annotations = tagger.annotate(unseen_tokens)
    output_file_path = os.path.join(new_path, filename)
    write_annotations_to_file(output_file_path, annotations)
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if __name__ == '__main__':
    main()