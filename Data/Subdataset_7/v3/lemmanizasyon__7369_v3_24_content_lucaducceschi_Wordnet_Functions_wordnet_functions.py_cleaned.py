import nltk
from nltk.corpus import wordnet as wn
def fonk1(b8):
    b1 = wn.b1(b8)
    b2 = [synset for synset in b1 if b8 in str(synset)]
    def fonk2(synset):
        return synset.b9()
    b3 = [list(synset.closure(find_hyponyms, depth=1)) for synset in b2]
    return b3
def fonk3(b8):
    b1 = wn.b1(b8)
    b4 = [str(synset) for synset in b1 if b8 in str(synset)]
    def fonk4(synset):
        return synset.b10()
    b5 = [list(wn.synset(synset).closure(find_hypernyms, depth=8)) for synset in b4]
    return b4, b5
def fonk5(b6):
    if b6 = = "NOUN":
        return "n"
    elif b6 = = "VERB":
        return "v"
    elif b6 = = "ADJ":
        return "a"
    elif b6 = = "ADV":
        return "r"
    else:
        return None
def fonk6(word_pos_tuple):
    word, b7 = word_pos_tuple
    if wn.morphy(word, fonk5(b7)) is None:
        return word, b7
    else:
        return wn.morphy(word, fonk5(b7)), b7
def fonk7(corpus):
    return [[fonk6(word_pos) for word_pos in line] for line in corpus]
b8 = "car"
b9 = fonk1(b8)
b10 = fonk3(b8)
print("Hyponyms:")
print(b9)
print("\nHypernyms:")
print(b10)