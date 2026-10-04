import nltk
from nltk.corpus import wordnet as wn
def fonk1(noun):
    b1 = wn.synsets(noun)
    b2 = [synset for synset in b1 if noun in synset.lemma_names()]
    def fonk2(synset):
        return synset.hyponyms()
    b3 = [list(synset.closure(hyponyms_closure, depth=1)) for synset in b2]
    return b3
def fonk3(noun):
    b1 = wn.synsets(noun)
    b4 = [str(synset) for synset in b1 if noun in synset.lemma_names()]
    def fonk4(synset):
        return synset.hypernyms()
    b5 = [list(wn.synset(synset_str).closure(hypernyms_closure, depth=8)) for synset_str in b4]
    return b4, b5
def fonk5(tag):
    b6 = {"NOUN": "n", "VERB": "v", "ADJ": "a", "ADV": "r"}
    return b6.get(tag)
def fonk6(word_tuple):
    b7 = wn.morphy(word_tuple[0], fonk5(word_tuple[1]))
    return (b7, word_tuple[1]) if b7 else word_tuple
def fonk7(corpus):
    return [[fonk6(word) for word in line] for line in corpus]