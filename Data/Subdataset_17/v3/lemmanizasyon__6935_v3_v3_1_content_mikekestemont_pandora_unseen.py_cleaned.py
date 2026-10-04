from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def load_tagger_model(model_dir='models/new_cg'):
    print('::: Loading Tagger Model :::')
    return Tagger(load=True, model_dir=model_dir)
def annotate_file(tagger, orig_path, new_path, filename):
    print(f'\t + Annotating {filename}')
    unseen_tokens = pandora.utils.load_unannotated_file(
        os.path.join(orig_path, filename),
        nb_instances=None,
        tokenized_input=False
    )
    annotations = tagger.annotate(unseen_tokens)
    output_file_path = os.path.join(new_path, filename)
    write_annotations_to_file(output_file_path, annotations)
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write(f'{token.lower()}\t{lemma.lower()}\t{pos.lower()}\n')
def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
def main():
    print('::: Annotation Started :::')
    tagger = load_tagger_model()
    print('::: Tagger loaded, now annotating :::')
    orig_path = 'data/limborch/orig/'
    new_path = 'data/limborch/tagged/'
    ensure_directory_exists(new_path)
    for filename in os.listdir(orig_path):
        if filename.endswith('.txt'):
            annotate_file(tagger, orig_path, new_path, filename)
    print('::: Annotation Ended :::')
if __name__ == '__main__':
    main()