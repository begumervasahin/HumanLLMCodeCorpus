import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
stop_words = set(stopwords.words("english"))
dictionary = enchant.Dict("en_US")
valid_words = set(nltk.corpus.words.words())
lemmatizer = WordNetLemmatizer()
with open("new_preprocessed.txt", "a") as output:
    with open('new_tweets.txt', 'r') as input_file:
        for line in input_file:
            tweet_text = line.split(',text:')[1]
            tweet_text = tweet_text.lower()
            tweet_text = ''.join(char for char in tweet_text if not char.isdigit() and char not in string.punctuation)
            cleaned_text = " ".join(
                word for word in tweet_text.split()
                if not word.startswith('@') and len(word) > 2 and dictionary.check(word)
            )
            tokenized_words = word_tokenize(cleaned_text)
            filtered_words = [word for word in tokenized_words if word not in stop_words]
            lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
            pos_tagged_words = nltk.pos_tag(lemmatized_words)
            final_words = [word for word, tag in pos_tagged_words if tag not in ('NNP', 'NNPS')]
            output.write(" ".join(final_words) + "\n")