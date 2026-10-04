import nltk
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def preprocess_text(text):
    porter_stemmer = nltk.PorterStemmer()
    words = text.split()
    filtered_words = [word.lower() for word in words if word.lower() not in sw.words('english')]
    stemmed_words = [porter_stemmer.stem(word) for word in filtered_words]
    return stemmed_words
def calculate_similarity(words1, words2):
    total_similarity = 0
    comparisons = 0
    for word1 in words1:
        synsets1 = wn.synsets(word1)
        if not synsets1:
            continue
        synset1 = synsets1[0]
        for word2 in words2:
            synsets2 = wn.synsets(word2)
            if not synsets2:
                continue
            synset2 = synsets2[0]
            similarity = synset1.path_similarity(synset2)
            if similarity is not None:
                total_similarity += similarity
                comparisons += 1
    return total_similarity / comparisons if comparisons > 0 else 0
def print_similarity(text1, text2):
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    similarity = calculate_similarity(words1, words2)
    print(f"Semantic similarity between '{text1}' and '{text2}': {similarity:.4f}")
print_similarity("I am loved by everyone", "Everyone loves me")