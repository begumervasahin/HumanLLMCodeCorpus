from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def annotate_files(input_dir, output_dir, tagger):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            annotate_file(input_dir, output_dir, filename, tagger)
def annotate_file(input_dir, output_dir, filename, tagger):
    print(f'\t + Annotating {filename}')
    input_file_path = os.path.join(input_dir, filename)
    unseen_tokens = pandora.utils.load_unannotated_file(
        input_file_path,
        nb_instances=None,
        tokenized_input=False
    )
    annotations = tagger.annotate(unseen_tokens)
    output_file_path = os.path.join(output_dir, filename)
    write_annotations_to_file(output_file_path, annotations)
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
def main():
    print('::: Annotation Started :::')
    tagger = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded, now annotating...')
    input_dir = 'data/limborch/orig/'
    output_dir = 'data/limborch/tagged/'
    annotate_files(input_dir, output_dir, tagger)
    print('::: Annotation Ended :::')
if __name__ == '__main__':
    main()