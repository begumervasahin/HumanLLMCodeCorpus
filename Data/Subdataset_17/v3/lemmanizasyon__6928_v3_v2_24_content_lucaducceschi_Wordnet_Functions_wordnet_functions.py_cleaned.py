import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def get_hyponyms(noun):
    synsets_with_noun = wn.synsets(noun)
    filtered_synsets = [synset for synset in synsets_with_noun if noun in synset.lemma_names()]
    def hyponyms_closure(synset):
        return synset.hyponyms()
    hyponyms_list = [list(synset.closure(hyponyms_closure, depth=1)) for synset in filtered_synsets]
    return hyponyms_list
def get_hypernyms(noun):
    synsets_with_noun = wn.synsets(noun)
    synset_strings = [str(synset) for synset in synsets_with_noun if noun in synset.lemma_names()]
    def hypernyms_closure(synset):
        return synset.hypernyms()
    hypernyms_list = [list(wn.synset(synset_str).closure(hypernyms_closure, depth=8)) for synset_str in synset_strings]
    return synset_strings, hypernyms_list
def universal_pos_converter(tag):
    if tag.startswith("NN"):
        return "n"
    elif tag.startswith("VB"):
        return "v"
    elif tag.startswith("JJ"):
        return "a"
    elif tag.startswith("RB"):
        return "r"
    else:
        return None
def lemmatize_word(word_tuple):
    word, tag = word_tuple
    lemma = wn.morphy(word, universal_pos_converter(tag))
    if lemma is None:
        return word, tag
    else:
        return lemma, tag
def tag_text(corpus):
    lemmatized_corpus = []
    for sentence in corpus:
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        lemmatized_sentence = [lemmatize_word(word) for word in pos_tags]
        lemmatized_corpus.append(lemmatized_sentence)
    return lemmatized_corpus
if __name__ == "__main__":
    noun = "dog"
    print(f"Hyponyms of '{noun}':")
    hyponyms = get_hyponyms(noun)
    for idx, hyps in enumerate(hyponyms):
        print(f"Synset {idx + 1}: {[hyp.name() for hyp in hyps]}")
    print(f"Hypernyms of '{noun}':")
    synset_strings, hypernyms_list = get_hypernyms(noun)
    for idx, (synset_str, hypernyms) in enumerate(zip(synset_strings, hypernyms_list)):
        print(f"Synset {idx + 1}: {synset_str}")
        print(f"Hypernyms: {[hyp.name() for hyp in hypernyms]}")
    corpus = ["The quick brown fox jumps over the lazy dog.", "The dog barked loudly."]
    lemmatized_text = tag_text(corpus)
    print("Lemmatized text:")
    for sentence in lemmatized_text:
        print(sentence)