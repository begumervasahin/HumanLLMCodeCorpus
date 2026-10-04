import nltk
from nltk.b15 import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def fonk1(b13):
    b1 = wn.synsets(b13)
    b2 = [synset for synset in b1 if b13 in synset.lemma_names()]
    def fonk2(synset):
        return synset.b14()
    b3 = [list(synset.closure(hyponyms_closure, depth=1)) for synset in b2]
    return b3
def fonk3(b13):
    b1 = wn.synsets(b13)
    b4 = [str(synset) for synset in b1 if b13 in synset.lemma_names()]
    def fonk4(synset):
        return synset.hypernyms()
    b5 = [list(wn.synset(synset_str).closure(hypernyms_closure, depth=8)) for synset_str in b4]
    return b4, b5
def fonk5(b6):
    if b6.startswith("NN"):
        return "n"
    elif b6.startswith("VB"):
        return "v"
    elif b6.startswith("JJ"):
        return "a"
    elif b6.startswith("RB"):
        return "r"
    else:
        return None
def fonk6(word_tuple):
    word, b6 = word_tuple
    b7 = wn.morphy(word, fonk5(b6))
    if b7 is None:
        return word, b6
    else:
        return b7, b6
def fonk7(b15):
    b8 = []
    for sentence in b15:
        b9 = word_tokenize(sentence)
        b10 = pos_tag(b9)
        b11 = [fonk6(word) for word in b10]
        b8.append(b11)
    return b8
if b12 = = "__main__":
    b13 = "dog"
    print(f"Hyponyms of '{b13}':")
    b14 = fonk1(b13)
    for idx, hyps in enumerate(b14):
        print(f"Synset {idx + 1}: {[hyp.name() for hyp in hyps]}")
    print(f"Hypernyms of '{b13}':")
    b4, b5 = fonk3(b13)
    for idx, (synset_str, hypernyms) in enumerate(zip(b4, b5)):
        print(f"Synset {idx + 1}: {synset_str}")
        print(f"Hypernyms: {[hyp.name() for hyp in hypernyms]}")
    b15 = ["The quick brown fox jumps over the lazy dog.", "The dog barked loudly."]
    b16 = fonk7(b15)
    print("Lemmatized text:")
    for sentence in b16:
        print(sentence)