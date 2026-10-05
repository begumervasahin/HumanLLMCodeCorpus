import nltk
import random
import pickle
from nltk.corpus import stopwords, wordnet, movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    return [word for word in tokens if word.lower() not in stop_words]
def stem_words(words):
    ps = PorterStemmer()
    return [ps.stem(word) for word in words]
def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word)
def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    return synonyms, antonyms
def calculate_similarity(word1, word2):
    synset1 = wordnet.synsets(word1)
    synset2 = wordnet.synsets(word2)
    if synset1 and synset2:
        return synset1[0].wup_similarity(synset2[0])
    return None
def extract_features(document, word_features):
    document_words = set(document)
    features = {word: (word in document_words) for word in word_features}
    return features
def train_classifier(training_set):
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier
def evaluate_classifier(classifier, testing_set):
    accuracy = nltk.classify.accuracy(classifier, testing_set) * 100
    print("Classifier accuracy percent:", accuracy)
    classifier.show_most_informative_features(15)
def save_classifier(classifier, filename):
    with open(filename, "wb") as save_file:
        pickle.dump(classifier, save_file)
def load_classifier(filename):
    with open(filename, "rb") as load_file:
        classifier = pickle.load(load_file)
    return classifier
def main():
    sentence = input("Enter a sentence: ")
    tokens = preprocess_text(sentence)
    stemmed_words = stem_words(tokens)
    lemmatized_word = lemmatize_word("cats")
    synonyms, antonyms = get_synonyms_antonyms("good")
    similarity = calculate_similarity("ship", "boat")
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words.keys())[:3000]
    featuresets = [(extract_features(rev, word_features), category) for (rev, category) in documents]
    training_set = featuresets[:1900]
    testing_set = featuresets[1900:]
    classifier = train_classifier(training_set)
    evaluate_classifier(classifier, testing_set)
    save_classifier(classifier, "naivebayes.pickle")
    loaded_classifier = load_classifier("naivebayes.pickle")
if __name__ == "__main__":
    main()