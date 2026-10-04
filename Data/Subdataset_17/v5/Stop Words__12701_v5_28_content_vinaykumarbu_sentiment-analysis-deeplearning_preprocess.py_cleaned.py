import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import WordNetLemmatizer
import enchant
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
spell_checker = enchant.Dict("en_US")
valid_words = set(words.words())
def preprocess_text(text):
    text = text.split(',text:')[1].strip().lower()
    text = ''.join([char for char in text if not char.isdigit() and char not in string.punctuation])
    words_list = [word for word in text.split() if not word.startswith('@') and len(word) > 2 and spell_checker.check(word)]
    tokenized_words = word_tokenize(" ".join(words_list))
    filtered_words = [word for word in tokenized_words if word not in stop_words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    tagged_sentence = nltk.pos_tag(lemmatized_words)
    final_words = [word for word, tag in tagged_sentence if tag not in ('NNP', 'NNPS')]
    return final_words
def main():
    input_file = 'new_tweets.txt'
    output_file = 'new_preprocessed.txt'
    with open(input_file, 'r') as f, open(output_file, 'a') as output:
        for text in f:
            processed_words = preprocess_text(text)
            output.write(" ".join(processed_words) + "\n")
if __name__ == "__main__":
    main()