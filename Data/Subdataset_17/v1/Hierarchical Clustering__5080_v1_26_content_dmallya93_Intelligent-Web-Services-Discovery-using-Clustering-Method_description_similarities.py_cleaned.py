import nltk
import re
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
nltk.download('stopwords')
nltk.download('wordnet')
def get_words(text):
    words = text.split()
    porter = nltk.PorterStemmer()
    filtered_words = [word.lower() for word in words if word.lower() not in sw.words('english')]
    stemmed_words = [porter.stem(word) for word in filtered_words]
    return stemmed_words
def sim_desc(text1, text2):
    words1 = get_words(text1)
    words2 = get_words(text2)
    sim_desc_total = 0
    try:
        for word1 in words1:
            syn1 = wn.synsets(word1)
            if syn1:
                syn1 = syn1[0]
                for word2 in words2:
                    syn2 = wn.synsets(word2)
                    if syn2:
                        syn2 = syn2[0]
                        similarity = syn1.path_similarity(syn2)
                        if similarity is not None:
                            sim_desc_total += similarity
    except Exception as e:
        print(f"Error: {str(e)}")
    if len(words1) > 0 and len(words2) > 0:
        sim_desc_avg = sim_desc_total / (len(words1) * len(words2))
    else:
        sim_desc_avg = 0
    print(f"Semantic similarity: {sim_desc_avg}")
    return sim_desc_avg
sim_desc("I am loved by everyone", "Everyone loves me")