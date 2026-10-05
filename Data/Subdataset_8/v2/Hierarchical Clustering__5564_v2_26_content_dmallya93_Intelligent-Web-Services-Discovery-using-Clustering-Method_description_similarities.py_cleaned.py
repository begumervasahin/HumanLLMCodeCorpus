import os
import re
import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def get_words(text):
    words = text.split(" ")
    filtered_words = []
    stop_words = set(sw.words())
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word.lower())
    porter = nltk.PorterStemmer()
    stemmed_words = [porter.stem(t) for t in filtered_words]
    return stemmed_words
def semantic_similarity(sentence1, sentence2):
    words1 = get_words(sentence1)
    words2 = get_words(sentence2)
    total_similarity = 0
    for word1 in words1:
        synsets1 = wn.synsets(word1)
        if synsets1:
            synset1 = synsets1[0]
            for word2 in words2:
                synsets2 = wn.synsets(word2)
                if synsets2:
                    synset2 = synsets2[0]
                    path_similarity = synset1.path_similarity(synset2)
                    if path_similarity:
                        total_similarity += path_similarity
    num_pairs = len(words1) * len(words2)
    if num_pairs == 0:
        return 0.0
    return total_similarity / num_pairs
if __name__ == "__main__":
    sentence1 = "I am loved by everyone"
    sentence2 = "Everyone loves me"
    similarity_score = semantic_similarity(sentence1, sentence2)
    print("Semantic similarity score:", similarity_score)