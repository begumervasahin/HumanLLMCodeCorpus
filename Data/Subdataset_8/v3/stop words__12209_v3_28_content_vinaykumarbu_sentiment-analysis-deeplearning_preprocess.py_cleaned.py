import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
english_dict = enchant.Dict("en_US")
stop_words = set(stopwords.words("english"))
with open("new_preprocessed.txt", "a") as output_file:
    with open('new_tweets.txt', 'r') as input_file:
        for line in input_file:
            tweet_text = line.split(',text:')[1]
            cleaned_tweet_text = preprocess_tweet(tweet_text)
            tokenized_words = word_tokenize(cleaned_tweet_text)
            filtered_words = filter_stopwords(tokenized_words)
            lemmatized_words = lemmatize_words(filtered_words)
            edited_words = filter_proper_nouns(lemmatized_words)
            output_file.write(" ".join(edited_words) + "\n")
def preprocess_tweet(tweet_text):
    tweet_text_lowercase = tweet_text.lower()
    cleaned_tweet_text = ''.join([char for char in tweet_text_lowercase if not char.isdigit() and char not in string.punctuation])
    clean_tweet_text = " ".join(word for word in cleaned_tweet_text.split() if is_valid_word(word))
    return clean_tweet_text
def is_valid_word(word):
    return not word.startswith('@') and len(word) > 2 and english_dict.check(word)
def filter_stopwords(words):
    return [word for word in words if word not in stop_words]
def lemmatize_words(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words]
def filter_proper_nouns(words):
    tagged_words = nltk.tag.pos_tag(words)
    return [word for word, tag in tagged_words if tag != 'NNP' and tag != 'NNPS']