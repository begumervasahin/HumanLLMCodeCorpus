from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def load_tagger_model(model_dir='models/new_cg'):
    print('::: Loading Tagger Model :::')
    return Tagger(load=True, model_dir=model_dir)
def load_unannotated_data(file_path):
    return pandora.utils.load_unannotated_file(file_path, nb_instances=None, tokenized_input=False)
def annotate_tokens(tagger, unseen_tokens):
    print('::: Annotating Tokens :::')
    return tagger.annotate(unseen_tokens)
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
def process_file(filename, orig_path, new_path, tagger):
    input_file_path = os.path.join(orig_path, filename)
    unseen_tokens = load_unannotated_data(input_file_path)
    annotations = annotate_tokens(tagger, unseen_tokens)
    output_file_path = os.path.join(new_path, filename)
    write_annotations_to_file(output_file_path, annotations)
def process_files(orig_path, new_path, tagger):
    print('::: Annotation Process Started :::')
    for filename in os.listdir(orig_path):
        if filename.endswith('.txt'):
            print(f'\t + Annotating {filename}')
            process_file(filename, orig_path, new_path, tagger)
    print('::: Annotation Process Ended :::')
def main():
    tagger = load_tagger_model()
    orig_path = 'data/limborch/orig/'
    new_path = 'data/limborch/tagged/'
    process_files(orig_path, new_path, tagger)
if __name__ == '__main__':
    main()