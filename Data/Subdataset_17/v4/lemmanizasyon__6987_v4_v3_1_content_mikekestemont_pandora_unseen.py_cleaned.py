from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def load_tagger_model():
    print('::: Loading Tagger Model :::')
    return Tagger(load=True, model_dir='models/new_cg')
def annotate_file(tagger, orig_path, new_path, filename):
    print('\t + Annotating', filename)
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
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
def main():
    print('::: Annotation Started :::')
    tagger = load_tagger_model()
    print('::: Tagger loaded, now annotating :::')
    orig_path = 'data/limborch/orig/'
    new_path = 'data/limborch/tagged/'
    os.makedirs(new_path, exist_ok=True)
    for filename in os.listdir(orig_path):
        if filename.endswith('.txt'):
            annotate_file(tagger, orig_path, new_path, filename)
    print('::: Annotation Ended :::')
if __name__ == '__main__':
    main()