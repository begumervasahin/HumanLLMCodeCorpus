import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import enchant
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
stop_words = set(stopwords.words("english"))
english_dict = enchant.Dict("en_US")
with open('new_tweets.txt', 'r') as input_file, open("new_preprocessed.txt", "a") as output_file:
    for line in input_file:
        text = line.split(',text:')[1]
        clean_text = ''.join([char.lower() for char in text if not char.isdigit() and char not in string.punctuation])
        filtered_text = " ".join(word for word in clean_text.split() if not word.startswith('@') and len(word) > 2 and english_dict.check(word))
        tokenized_words = word_tokenize(filtered_text)
        filtered_words = [word for word in tokenized_words if word not in stop_words]
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        tagged_words = nltk.tag.pos_tag(lemmatized_words)
        edited_words = [word for word, tag in tagged_words if tag not in ('NNP', 'NNPS')]
        output_file.write(" ".join(edited_words))
        output_file.write("\n")