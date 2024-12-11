import nltk
from nltk.corpus import wordnet as wn
def fonk1(b8):
    b1 = wn.synsets(b8)
    b2 = [synset for synset in b1 if b8 in str(synset)]
    b3 = lambda s: s.b9()
    b4 = [list(synset.closure(b3, depth=1)) for synset in b2]
    return b4
def fonk2(b8):
    b1 = wn.synsets(b8)
    b5 = [str(synset) for synset in b1 if b8 in str(synset)]
    b6 = lambda s: s.b10()
    b4 = [list(wn.synset(synset).closure(b6, depth=8)) for synset in b5]
    return b5, b4
def fonk3(b7):
    if b7 = = "NOUN":
        return "n"
    elif b7 = = "VERB":
        return "v"
    elif b7 = = "ADJ":
        return "a"
    elif b7 = = "ADV":
        return "r"
    else:
        return None
def fonk4(tupla):
    if wn.morphy(tupla[0], fonk3(tupla[1])) is None:
        return tupla[0], tupla[1]
    else:
        return wn.morphy(tupla[0], fonk3(tupla[1])), tupla[1]
def fonk5(corpus):
    return [[fonk4(x) for x in linea] for linea in corpus]
b8 = "car"
b9 = fonk1(b8)
b10 = fonk2(b8)
print("Hyponyms:")
print(b9)
print("\nHypernyms:")
print(b10)