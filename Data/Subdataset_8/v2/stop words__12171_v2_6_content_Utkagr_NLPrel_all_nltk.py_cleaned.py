import nltk
import random
import pickle
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('state_union')
nltk.download('gutenberg')
nltk.download('wordnet')
nltk.download('movie_reviews')
from nltk.corpus import stopwords, state_union, gutenberg, wordnet, movie_reviews
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word not in stop_words]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
tagged_words = nltk.pos_tag(tokens)
named_entities = nltk.ne_chunk(tagged_words)
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized_sentences = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for sentence in tokenized_sentences:
            words = word_tokenize(sentence)
            tagged = nltk.pos_tag(words)
            chunkGram = r
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
    except Exception as e:
        print(str(e))
example_string = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
ages = re.findall(r'\d{1,3}', example_string)
names = re.findall(r'[A-Z][a-z]*', example_string)
print("Ages:", ages)
print("Names:", names)
synsets = wordnet.synsets("program")
print("Synsets:", synsets)
print("First lemma name:", synsets[0].lemmas()[0].name())
print("Definition:", synsets[0].definition())
print("Examples:", synsets[0].examples())
ship_synset = wordnet.synset("ship.n.01")
boat_synset = wordnet.synset("boat.n.01")
similarity = ship_synset.wup_similarity(boat_synset)
print("Similarity between 'ship' and 'boat':", similarity)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(word.lower() for word in movie_reviews.words())
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