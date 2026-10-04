import nltk
from nltk.corpus import wordnet as wn
def get_hyponyms(noun):
    synsets_with_noun = wn.synsets(noun)
    filtered_synsets = [synset for synset in synsets_with_noun if noun in synset.lemma_names()]
    def hyponyms_closure(synset):
        return synset.hyponyms()
    hyponyms_list = [list(synset.closure(hyponyms_closure, depth=1)) for synset in filtered_synsets]
    return hyponyms_list
def get_hypernyms(noun):
    synsets_with_noun = wn.synsets(noun)
    synset_strings = [str(synset) for synset in synsets_with_noun if noun in synset.lemma_names()]
    def hypernyms_closure(synset):
        return synset.hypernyms()
    hypernyms_list = [list(wn.synset(synset_str).closure(hypernyms_closure, depth=8)) for synset_str in synset_strings]
    return synset_strings, hypernyms_list
def universal_pos_converter(tag):
    if tag == "NOUN":
        return "n"
    elif tag == "VERB":
        return "v"
    elif tag == "ADJ":
        return "a"
    elif tag == "ADV":
        return "r"
    else:
        return None
def lemmatize_word(word_tuple):
    lemma = wn.morphy(word_tuple[0], universal_pos_converter(word_tuple[1]))
    if lemma is None:
        return word_tuple[0], word_tuple[1]
    else:
        return lemma, word_tuple[1]
def tag_text(corpus):
    return [[lemmatize_word(word) for word in line] for line in corpus]