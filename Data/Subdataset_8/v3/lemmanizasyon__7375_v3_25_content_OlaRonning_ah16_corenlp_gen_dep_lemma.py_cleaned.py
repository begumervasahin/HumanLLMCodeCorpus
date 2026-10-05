from __future__ import print_function
import json
import sys
from stanfordnlp.server import CoreNLPClient
def fix_dependency_index(dependency):
    ''' Fixes off-by-one error in dependency suffix index '''
    def adjust_index(index):
        return [index[0], str(int(index[1]) - 1)]
    relation, index1, index2 = dependency
    index1_adjusted = adjust_index(index1.split('-'))
    index2_adjusted = adjust_index(index2.split('-'))
    return [relation, index1_adjusted, index2_adjusted]
def extract_article_sentences(example):
    ''' Extracts the match and the previous sentence from the example '''
    before_sentences = [sentence['string'] for sentence in example['before']]
    match_sentence = example['match']['sentence']['string']
    candidate_sentences = before_sentences + [match_sentence]
    return candidate_sentences[-2:]
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gen_dep_lemma.py <Corpus File>", file=sys.stderr)
        sys.exit(1)
    with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','depparse'], timeout=60000, memory='16G') as client:
        corpus_file_path = sys.argv[1]
        annotated_data = {}
        with open(corpus_file_path, 'r') as corpus_file:
            for example_json in corpus_file:
                example = json.loads(example_json)
                try:
                    sluice_id = "{0[file]}_{0[line]}_{0[treeNode]}".format(example['metadata'])
                    article_sentences = extract_article_sentences(example)
                except Exception as e:
                    print(f"Error processing example: {e}", file=sys.stderr)
                    continue
                annotated_data[sluice_id] = article_sentences
        output_file_path = 'dep_lemma.jsons'
        with open(output_file_path, 'w') as output_file:
            for sluice_id, article_sentences in annotated_data.items():
                for sentence in article_sentences:
                    try:
                        annotation = client.annotate(sentence)
                        lemmas = [word.lemma for sent in annotation.sentences for word in sent.words]
                        output_dict = {'sluiceId': sluice_id, 'dependencies': [fix_dependency_index(dep) for dep in annotation.dependencies], 'sentence': sentence, 'lemmas': lemmas}
                        print(json.dumps(output_dict), file=output_file)
                    except Exception as e:
                        print(f"Error processing sentence '{sentence}': {e}", file=sys.stderr)
                        continue