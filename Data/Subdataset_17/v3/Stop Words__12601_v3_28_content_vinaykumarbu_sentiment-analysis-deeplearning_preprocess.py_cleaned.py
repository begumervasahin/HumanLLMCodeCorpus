import string
import nltk
import enchant
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
stop_words = set(stopwords.words("english"))
dictionary = enchant.Dict("en_US")
lemmatizer = WordNetLemmatizer()
def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = ''.join(char for char in tweet if not char.isdigit() and char not in string.punctuation)
    cleaned_text = " ".join(
        word for word in tweet.split()
        if not word.startswith('@') and len(word) > 2 and dictionary.check(word)
    )
    tokenized_words = word_tokenize(cleaned_text)
    filtered_words = [word for word in tokenized_words if word not in stop_words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    pos_tagged_words = nltk.pos_tag(lemmatized_words)
    final_words = [word for word, tag in pos_tagged_words if tag not in ('NNP', 'NNPS')]
    return " ".join(final_words)
def process_tweets(input_file_path, output_file_path):
    with open(output_file_path, "a") as output_file:
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                try:
                    tweet_text = line.split(',text:')[1]
                    processed_tweet = preprocess_tweet(tweet_text)
                    output_file.write(processed_tweet + "\n")
                except IndexError:
                    continue
process_tweets('new_tweets.txt', 'new_preprocessed.txt')