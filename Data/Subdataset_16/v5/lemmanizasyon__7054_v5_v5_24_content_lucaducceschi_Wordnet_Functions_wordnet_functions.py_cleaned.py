import nltk
from nltk.corpus import wordnet as wn
def fonk1(b9):
    b1 = wn.b1(b9)
    b2 = [synset for synset in b1 if b9 in synset.lemma_names()]
    b3 = [list(synset.closure(lambda s: s.hyponyms(), depth=1)) for synset in b2]
    return b3
def fonk2(b9):
    b1 = wn.b1(b9)
    b2 = [str(synset) for synset in b1 if b9 in synset.lemma_names()]
    b4 = [list(wn.synset(synset_str).closure(lambda s: s.hypernyms(), depth=8)) for synset_str in b2]
    return b2, b4
def fonk3(tag):
    b5 = {
        "NOUN": "n",
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r"
    }
    return b5.get(tag, None)
def fonk4(word, pos_tag):
    b6 = fonk3(pos_tag)
    b7 = wn.morphy(word, b6) if b6 else word
    return b7 if b7 else word, pos_tag
def fonk5(corpus):
    return [[fonk4(word, pos_tag) for word, pos_tag in sentence] for sentence in corpus]
if b8 = = "__main__":
    b9 = "dog"
    print(f"Hyponyms of '{b9}': {fonk1(b9)}")
    print(f"Hypernyms of '{b9}': {fonk2(b9)}")
    b10 = [[('running', 'VERB'), ('quickly', 'ADV')], [('dogs', 'NOUN'), ('barking', 'VERB')]]
    print(f"Lemmatized text: {fonk5(b10)}")