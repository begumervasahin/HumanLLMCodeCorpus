import nltk
from nltk.corpus import wordnet as wn
def get_hyponyms(noun):
    synsets = wn.synsets(noun)
    filtered_synsets = [synset for synset in synsets if noun in synset.lemma_names()]
    hyponyms_list = [list(synset.hyponyms()) for synset in filtered_synsets]
    return hyponyms_list
def get_hypernyms(noun):
    synsets = wn.synsets(noun)
    synset_strings = [str(synset) for synset in synsets if noun in synset.lemma_names()]
    hypernyms_list = [list(wn.synset(synset_str).hypernyms()) for synset_str in synset_strings]
    return synset_strings, hypernyms_list
def universal_pos_converter(tag):
    pos_conversion = {
        "NOUN": "n",
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r"
    }
    return pos_conversion.get(tag)
def lemmatize_word(word_tuple):
    word, pos = word_tuple
    lemma = wn.morphy(word, universal_pos_converter(pos))
    return (lemma if lemma else word, pos)
def tag_text(corpus):
    return [[lemmatize_word(word) for word in line] for line in corpus]