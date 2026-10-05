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
output_file = open("new_preprocessed.txt", "a")
with open('new_tweets.txt', 'r') as input_file:
    for line in input_file:
        tweet_text = line.split(',text:')[1]
        tweet_text_lowercase = tweet_text.lower()
        cleaned_tweet_text = ''.join([char for char in tweet_text_lowercase if not char.isdigit() and char not in string.punctuation])
        clean_tweet_text = ""
        for word in cleaned_tweet_text.split(' '):
            if (not word.startswith('@') and len(word) > 2 and english_dict.check(word)):
                clean_tweet_text += " " + word
        tokenized_words = word_tokenize(clean_tweet_text)
        filtered_words = [word for word in tokenized_words if word not in stop_words]
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        tagged_words = nltk.tag.pos_tag(lemmatized_words)
        edited_words = [word for word, tag in tagged_words if tag != 'NNP' and tag != 'NNPS']
        output_file.write(" ".join(edited_words) + "\n")
output_file.close()