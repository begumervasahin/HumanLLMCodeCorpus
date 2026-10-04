import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import enchant
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
d = enchant.Dict("en_US")
valid_words = set(words.words())
with open('new_tweets.txt', 'r') as f, open("new_preprocessed.txt", "a") as output:
    for text in f:
        text = text.split(',text:')[1].strip()
        input_str = text.lower()
        input_str = ''.join([char for char in input_str if not char.isdigit() and char not in string.punctuation])
        cleaned_text = " ".join([word for word in input_str.split() if not word.startswith('@') and len(word) > 2 and d.check(word)])
        tokenized_words = word_tokenize(cleaned_text)
        filtered_words = [word for word in tokenized_words if word not in stop_words]
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        tagged_sentence = nltk.pos_tag(lemmatized_words)
        final_words = [word for word, tag in tagged_sentence if tag not in ('NNP', 'NNPS')]
        output.write(" ".join(final_words) + "\n")