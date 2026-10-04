import nltk
from nltk.corpus import wordnet as wn
def get_hyponyms(noun):
    synsets = wn.synsets(noun)
    filtered_synsets = [synset for synset in synsets if noun in synset.lemma_names()]
    hyponyms_list = [list(synset.closure(lambda s: s.hyponyms(), depth=1)) for synset in filtered_synsets]
    return hyponyms_list
def get_hypernyms(noun):
    synsets = wn.synsets(noun)
    filtered_synsets = [str(synset) for synset in synsets if noun in synset.lemma_names()]
    hypernyms_list = [list(wn.synset(synset_str).closure(lambda s: s.hypernyms(), depth=8)) for synset_str in filtered_synsets]
    return filtered_synsets, hypernyms_list
def convert_pos_tag(tag):
    pos_tag_map = {
        "NOUN": "n",
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r"
    }
    return pos_tag_map.get(tag, None)
def lemmatize(word, pos_tag):
    wn_pos = convert_pos_tag(pos_tag)
    lemma = wn.morphy(word, wn_pos) if wn_pos else word
    return lemma if lemma else word, pos_tag
def lemmatize_corpus(corpus):
    return [[lemmatize(word, pos_tag) for word, pos_tag in sentence] for sentence in corpus]
if __name__ == "__main__":
    noun = "dog"
    print(f"Hyponyms of '{noun}': {get_hyponyms(noun)}")
    print(f"Hypernyms of '{noun}': {get_hypernyms(noun)}")
    sample_corpus = [[('running', 'VERB'), ('quickly', 'ADV')], [('dogs', 'NOUN'), ('barking', 'VERB')]]
    print(f"Lemmatized text: {lemmatize_corpus(sample_corpus)}")