import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def preprocess_text(text):
    words = text.split(" ")
    stop_words = set(sw.words())
    porter = nltk.PorterStemmer()
    filtered_words = [porter.stem(word.lower()) for word in words if word.lower() not in stop_words]
    return filtered_words
def calculate_similarity(word_list1, word_list2):
    total_similarity = 0
    for word1 in word_list1:
        synsets1 = wn.synsets(word1)
        if synsets1:
            synset1 = synsets1[0]
            for word2 in word_list2:
                synsets2 = wn.synsets(word2)
                if synsets2:
                    synset2 = synsets2[0]
                    path_similarity = synset1.path_similarity(synset2)
                    if path_similarity:
                        total_similarity += path_similarity
    num_pairs = len(word_list1) * len(word_list2)
    if num_pairs == 0:
        return 0.0
    return total_similarity / num_pairs
def semantic_similarity(sentence1, sentence2):
    words1 = preprocess_text(sentence1)
    words2 = preprocess_text(sentence2)
    similarity_score = calculate_similarity(words1, words2)
    return similarity_score
if __name__ == "__main__":
    sentence1 = "I am loved by everyone"
    sentence2 = "Everyone loves me"
    similarity_score = semantic_similarity(sentence1, sentence2)
    print("Semantic similarity score:", similarity_score)