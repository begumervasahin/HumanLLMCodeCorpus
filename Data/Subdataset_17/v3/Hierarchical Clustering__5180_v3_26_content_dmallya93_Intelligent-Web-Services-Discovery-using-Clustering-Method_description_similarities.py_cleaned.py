import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def preprocess_text(text):
    porter_stemmer = nltk.PorterStemmer()
    filtered_words = [
        porter_stemmer.stem(word.lower())
        for word in text.split()
        if word.lower() not in stopwords.words('english')
    ]
    return filtered_words
def calculate_similarity(text1, text2):
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    total_similarity = 0
    try:
        for word1 in words1:
            synsets1 = wn.synsets(word1)
            if synsets1:
                synset1 = synsets1[0]
                for word2 in words2:
                    synsets2 = wn.synsets(word2)
                    if synsets2:
                        synset2 = synsets2[0]
                        similarity = synset1.path_similarity(synset2)
                        if similarity:
                            total_similarity += similarity
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    num_comparisons = len(words1) * len(words2)
    average_similarity = total_similarity / num_comparisons if num_comparisons > 0 else 0
    print(f"Semantic similarity: {average_similarity:.4f}")
    return average_similarity
calculate_similarity("I am loved by everyone", "Everyone loves me")