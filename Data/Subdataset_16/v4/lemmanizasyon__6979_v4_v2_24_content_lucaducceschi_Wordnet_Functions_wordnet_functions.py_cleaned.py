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
    b6 = {
        "NOUN": "n",
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r"
    }
    return b6.get(tag, None)
def fonk6(word_tuple):
    word, b7 = word_tuple
    b8 = wn.morphy(word, fonk5(b7))
    return (b8 if b8 is not None else word, b7)
def fonk7(corpus):
    return [[fonk6(word) for word in line] for line in corpus]