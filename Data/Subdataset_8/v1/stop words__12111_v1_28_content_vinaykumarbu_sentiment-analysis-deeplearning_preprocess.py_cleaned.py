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
d = enchant.Dict("en_US")
stop_words = set(stopwords.words("english"))
output_file = open("new_preprocessed.txt", "a")
with open('new_tweets.txt', 'r') as input_file:
    for line in input_file:
        text = line.split(',text:')[1]
        input_str = text.lower()
        input_str = ''.join([i for i in input_str if not i.isdigit() and i not in string.punctuation])
        remove_names_str = ""
        for word in input_str.split(' '):
            if (not word.startswith('@') and len(word) > 2 and d.check(word)):
                remove_names_str += " " + word
        tokenized_word = word_tokenize(remove_names_str)
        filtered_sent = [w for w in tokenized_word if w not in stop_words]
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_sent]
        tagged_sentence = nltk.tag.pos_tag(lemmatized_words)
        edited_sentence = [word for word, tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']
        output_file.write(" ".join(edited_sentence) + "\n")
output_file.close()