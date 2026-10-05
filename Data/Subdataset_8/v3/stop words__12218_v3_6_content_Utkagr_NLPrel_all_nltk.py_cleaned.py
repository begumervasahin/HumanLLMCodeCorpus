import nltk
import random
import pickle
import re
def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('state_union')
    nltk.download('gutenberg')
    nltk.download('wordnet')
    nltk.download('movie_reviews')
def preprocess_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    stemmer = nltk.stem.PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
    tagged_words = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(tagged_words)
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens, filtered_tokens, stemmed_words, tagged_words, named_entities, lemmatized_words
def chunk_sentences(sample_text):
    train_text = nltk.corpus.state_union.raw("2005-GWBush.txt")
    custom_sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer(train_text)
    tokenized_sentences = custom_sent_tokenizer.tokenize(sample_text)
    for sentence in tokenized_sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        chunk_grammar = r
        chunk_parser = nltk.RegexpParser(chunk_grammar)
        chunked = chunk_parser.parse(tagged)
        print(chunked)
def extract_info_from_string(example_string):
    ages = re.findall(r'\d{1,3}', example_string)
    names = re.findall(r'[A-Z][a-z]*', example_string)
    print("Ages:", ages)
    print("Names:", names)
def analyze_wordnet():
    synsets = nltk.corpus.wordnet.synsets("program")
    print("Synsets:", synsets)
    print("First lemma name:", synsets[0].lemmas()[0].name())
    print("Definition:", synsets[0].definition())
    print("Examples:", synsets[0].examples())
    ship_synset = nltk.corpus.wordnet.synset("ship.n.01")
    boat_synset = nltk.corpus.wordnet.synset("boat.n.01")
    similarity = ship_synset.wup_similarity(boat_synset)
    print("Similarity between 'ship' and 'boat':", similarity)
def train_and_save_classifier():
    documents = [(list(nltk.corpus.movie_reviews.words(fileid)), category)
                 for category in nltk.corpus.movie_reviews.categories()
                 for fileid in nltk.corpus.movie_reviews.fileids(category)]
    random.shuffle(documents)
    all_words = nltk.FreqDist(word.lower() for word in nltk.corpus.movie_reviews.words())
    word_features = list(all_words.keys())[:3000]
    def find_features(document):
        words = set(document)
        features = {}
        for word in word_features:
            features[word] = (word in words)
        return features
    featuresets = [(find_features(review), category) for (review, category) in documents]
    training_set = featuresets[:1900]
    testing_set = featuresets[1900:]
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
    classifier.show_most_informative_features(15)
    with open("naivebayes.pickle", "wb") as save_classifier:
        pickle.dump(classifier, save_classifier)
    with open("naivebayes.pickle", "rb") as classifier_f:
        classifier = pickle.load(classifier_f)
def main():
    download_nltk_resources()
    sentence = input("Enter a sentence: ")
    tokens, filtered_tokens, stemmed_words, tagged_words, named_entities, lemmatized_words = preprocess_sentence(sentence)
    chunk_sentences(sample_text)
    extract_info_from_string(example_string)
    analyze_wordnet()
    train_and_save_classifier()
if __name__ == "__main__":
    main()