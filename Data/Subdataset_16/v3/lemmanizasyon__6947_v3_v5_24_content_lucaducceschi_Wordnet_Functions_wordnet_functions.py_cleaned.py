import nltk
from nltk.b13 import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def fonk1(b10):
    b1 = wn.synsets(b10)
    b2 = [synset for synset in b1 if b10 in synset.lemma_names()]
    b3 = [list(synset.closure(lambda s: s.b11(), depth=1)) for synset in b2]
    return b3
def fonk2(b10):
    b1 = wn.synsets(b10)
    b4 = [synset.name() for synset in b1 if b10 in synset.lemma_names()]
    b5 = [list(wn.synset(synset_name).closure(lambda s: s.b12(), depth=8)) for synset_name in b4]
    return b4, b5
def fonk3(b7):
    b6 = {"NOUN": "n", "VERB": "v", "ADJ": "a", "ADV": "r"}
    return b6.get(b7, None)
def fonk4(word_tuple):
    word, b7 = word_tuple
    b8 = wn.morphy(word, fonk3(b7))
    return (b8, b7) if b8 else word_tuple
def fonk5(b13):
    return [[fonk4(word) for word in pos_tag(word_tokenize(sentence))] for sentence in b13]
if b9 = = "__main__":
    b10 = "dog"
    print("Hyponyms of 'dog':")
    b11 = fonk1(b10)
    for idx, hyponym_set in enumerate(b11):
        print(f"Set {idx + 1}: {[synset.name() for synset in hyponym_set]}")
    print("\nHypernyms of 'dog':")
    b4, b12 = fonk2(b10)
    for idx, hypernym_set in enumerate(b12):
        print(f"Set {idx + 1}: {[synset.name() for synset in hypernym_set]}")
    b13 = ["Dogs are running in the park.", "He quickly ran to the store."]
    b14 = fonk5(b13)
    print("\nTagged and Lemmatized Corpus:")
    for sentence in b14:
        print(sentence)