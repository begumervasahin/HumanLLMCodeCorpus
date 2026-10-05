import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
import re
nltk.download('stopwords')
nltk.download('wordnet')
def get_words(text):
    words = text.split()
    filtered_words = []
    stop_words = set(sw.words())
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word.lower())
    porter = nltk.PorterStemmer()
    stemmed_words = [porter.stem(t) for t in filtered_words]
    return stemmed_words
def semantic_description_similarity(text1, text2):
    words1 = get_words(text1)
    words2 = get_words(text2)
    similarity = 0
    try:
        for word1 in words1:
            synsets1 = wn.synsets(word1.strip("\\n"))
            if synsets1:
                synset1 = synsets1[0]
                for word2 in words2:
                    synsets2 = wn.synsets(word2.strip("\\n"))
                    if synsets2:
                        synset2 = synsets2[0]
                        path_similarity = synset1.path_similarity(synset2)
                        if path_similarity:
                            similarity += path_similarity
        num_pairs = len(words1) * len(words2)
        if num_pairs == 0:
            return 0.0
        return similarity / num_pairs
    except Exception as e:
        print(str(e))
        return 0.0
if __name__ == "__main__":
    text1 = "I am loved by everyone"
    text2 = "Everyone loves me"
    similarity_score = semantic_description_similarity(text1, text2)
    print("Semantic similarity score:", similarity_score)