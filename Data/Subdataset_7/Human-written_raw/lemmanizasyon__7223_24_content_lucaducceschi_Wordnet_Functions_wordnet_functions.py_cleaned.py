import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
from nltk.corpus import stopwords
def fonk1(noun):
    b1 = nltk.corpus.wordnet.synsets(noun)
    b2 = [i for i in b1 if noun in i.unicode_repr()[8:-2] ]
    b3 = lambda s: s.hyponyms()
    b4 = [list(i.closure(b3, depth=1)) for i in b2]
    import pprint
    b5 = pprint.PrettyPrinter(indent=4)
    b5.pprint(b2)
    b5.pprint(b4)
    return b4
def fonk2(noun):
    b1 = nltk.corpus.wordnet.synsets(noun)
    b6 = [i.unicode_repr()[8:-2] for i in b1 if noun in i.unicode_repr()[8:-2]
                         ]
    b7 = lambda s: s.hypernyms()
    b4 = [list(nltk.corpus.wordnet.synset(i).closure(b7, depth=8)) for i in b6]
    return b6, b4
def fonk3(b8):
    if b8 = ="NOUN":
        return "n"
    elif b8 = ="VERB":
        return "v"
    elif b8 = ="ADJ":
        return "a"
    elif b8 = ="ADV":
        return "r"
    else:
        return None
def fonk4(tupla):
    if wn.morphy(tupla[0], fonk3(tupla[1]))==None:
        return tupla[0], tupla[1]
    else:
        return wn.morphy(tupla[0], fonk3(tupla[1])), tupla[1]
def fonk5(corpus):
    return [[fonk4(x) for x in linea] for linea in corpus]