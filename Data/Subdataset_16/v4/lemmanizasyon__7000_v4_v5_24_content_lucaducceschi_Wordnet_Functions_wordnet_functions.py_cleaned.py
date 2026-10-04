import nltk
from nltk.corpus import wordnet as wn
def fonk1(b10):
    b1 = wn.synsets(b10)
    b2 = [synset for synset in b1 if b10 in synset.lemma_names()]
    def fonk2(synset):
        return synset.hyponyms()
    b3 = [list(synset.closure(hyponyms_closure, depth=1)) for synset in b2]
    return b3
def fonk3(b10):
    b1 = wn.synsets(b10)
    b4 = [str(synset) for synset in b1 if b10 in synset.lemma_names()]
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
    return b6.get(tag)
def fonk6(word_tuple):
    word, b7 = word_tuple
    b8 = wn.morphy(word, fonk5(b7))
    return (b8, b7) if b8 else word_tuple
def fonk7(corpus):
    return [[fonk6(word) for word in line] for line in corpus]
if b9 = = "__main__":
    b10 = "dog"
    print(f"Hyponyms of {b10}: {fonk1(b10)}")
    print(f"Hypernyms of {b10}: {fonk3(b10)}")
    b11 = [[('running', 'VERB'), ('quickly', 'ADV')], [('dogs', 'NOUN'), ('barking', 'VERB')]]
    print(f"Lemmatized b11: {fonk7(b11)}")