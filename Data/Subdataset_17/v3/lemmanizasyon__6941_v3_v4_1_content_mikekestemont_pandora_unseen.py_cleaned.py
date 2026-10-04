from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: Annotation Process Started :::')
    tagger = load_tagger_model('models/new_cg')
    print('Tagger loaded. Now, annotating...')
    input_directory = 'data/limborch/orig/'
    output_directory = 'data/limborch/tagged/'
    ensure_directory_exists(output_directory)
    annotate_files_in_directory(input_directory, output_directory, tagger)
    print('::: Annotation Process Ended :::')
def load_tagger_model(model_directory):
    return Tagger(load=True, model_dir=model_directory)
def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
def annotate_files_in_directory(input_directory, output_directory, tagger):
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            print(f'\t + Annotating {filename}')
            annotate_and_save_file(input_directory, output_directory, filename, tagger)
def annotate_and_save_file(input_directory, output_directory, filename, tagger):
    file_path = os.path.join(input_directory, filename)
    tokens = load_tokens_from_file(file_path)
    annotations = tagger.annotate(tokens)
    save_annotations_to_file(output_directory, filename, annotations)
def load_tokens_from_file(file_path):
    return pandora.utils.load_unannotated_file(file_path, nb_instances=None, tokenized_input=False)
def save_annotations_to_file(output_directory, filename, annotations):
    output_file_path = os.path.join(output_directory, filename)
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write(f'{token.lower()}\t{lemma.lower()}\t{pos.lower()}\n')
if __name__ == '__main__':
    main()