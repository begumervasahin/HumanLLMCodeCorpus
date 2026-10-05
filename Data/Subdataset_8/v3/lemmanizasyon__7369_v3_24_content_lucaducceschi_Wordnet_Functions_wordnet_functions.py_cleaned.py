import nltk
from nltk.corpus import wordnet as wn
def get_hyponyms(noun):
    synsets = wn.synsets(noun)
    relevant_synsets = [synset for synset in synsets if noun in str(synset)]
    def find_hyponyms(synset):
        return synset.hyponyms()
    hyponym_lists = [list(synset.closure(find_hyponyms, depth=1)) for synset in relevant_synsets]
    return hyponym_lists
def get_hypernyms(noun):
    synsets = wn.synsets(noun)
    synset_strings = [str(synset) for synset in synsets if noun in str(synset)]
    def find_hypernyms(synset):
        return synset.hypernyms()
    hypernym_lists = [list(wn.synset(synset).closure(find_hypernyms, depth=8)) for synset in synset_strings]
    return synset_strings, hypernym_lists
def universal_pos_changer(tag):
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
def lemmatize_word(word_pos_tuple):
    word, pos = word_pos_tuple
    if wn.morphy(word, universal_pos_changer(pos)) is None:
        return word, pos
    else:
        return wn.morphy(word, universal_pos_changer(pos)), pos
def tag_text(corpus):
    return [[lemmatize_word(word_pos) for word_pos in line] for line in corpus]
noun = "car"
hyponyms = get_hyponyms(noun)
hypernyms = get_hypernyms(noun)
print("Hyponyms:")
print(hyponyms)
print("\nHypernyms:")
print(hypernyms)