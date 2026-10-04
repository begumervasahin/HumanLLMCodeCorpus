import nltk
from nltk.corpus import wordnet as wn
def fonk1(noun):
    b1 = wn.b1(noun)
    b2 = [synset for synset in b1 if noun in synset.lemma_names()]
    b3 = [list(synset.hyponyms()) for synset in b2]
    return b3
def fonk2(noun):
    b1 = wn.b1(noun)
    b4 = [str(synset) for synset in b1 if noun in synset.lemma_names()]
    b5 = [list(wn.synset(synset_str).hypernyms()) for synset_str in b4]
    return b4, b5
def fonk3(tag):
    b6 = {
        "NOUN": "n",
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r"
    }
    return b6.get(tag)
def fonk4(word_tuple):
    word, b7 = word_tuple
    b8 = wn.morphy(word, fonk3(b7))
    return (b8 if b8 else word, b7)
def fonk5(corpus):
    return [[fonk4(word) for word in line] for line in corpus]