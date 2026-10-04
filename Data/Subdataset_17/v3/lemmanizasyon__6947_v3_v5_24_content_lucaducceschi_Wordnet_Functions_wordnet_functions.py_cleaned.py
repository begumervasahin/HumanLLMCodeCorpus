import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def get_hyponyms(noun):
    synsets_with_noun = wn.synsets(noun)
    filtered_synsets = [synset for synset in synsets_with_noun if noun in synset.lemma_names()]
    hyponyms_list = [list(synset.closure(lambda s: s.hyponyms(), depth=1)) for synset in filtered_synsets]
    return hyponyms_list
def get_hypernyms(noun):
    synsets_with_noun = wn.synsets(noun)
    synset_names = [synset.name() for synset in synsets_with_noun if noun in synset.lemma_names()]
    hypernyms_list = [list(wn.synset(synset_name).closure(lambda s: s.hypernyms(), depth=8)) for synset_name in synset_names]
    return synset_names, hypernyms_list
def universal_pos_converter(tag):
    pos_tags_mapping = {"NOUN": "n", "VERB": "v", "ADJ": "a", "ADV": "r"}
    return pos_tags_mapping.get(tag, None)
def lemmatize_word(word_tuple):
    word, tag = word_tuple
    lemma = wn.morphy(word, universal_pos_converter(tag))
    return (lemma, tag) if lemma else word_tuple
def tag_and_lemmatize_text(corpus):
    return [[lemmatize_word(word) for word in pos_tag(word_tokenize(sentence))] for sentence in corpus]
if __name__ == "__main__":
    noun = "dog"
    print("Hyponyms of 'dog':")
    hyponyms = get_hyponyms(noun)
    for idx, hyponym_set in enumerate(hyponyms):
        print(f"Set {idx + 1}: {[synset.name() for synset in hyponym_set]}")
    print("\nHypernyms of 'dog':")
    synset_names, hypernyms = get_hypernyms(noun)
    for idx, hypernym_set in enumerate(hypernyms):
        print(f"Set {idx + 1}: {[synset.name() for synset in hypernym_set]}")
    corpus = ["Dogs are running in the park.", "He quickly ran to the store."]
    tagged_corpus = tag_and_lemmatize_text(corpus)
    print("\nTagged and Lemmatized Corpus:")
    for sentence in tagged_corpus:
        print(sentence)