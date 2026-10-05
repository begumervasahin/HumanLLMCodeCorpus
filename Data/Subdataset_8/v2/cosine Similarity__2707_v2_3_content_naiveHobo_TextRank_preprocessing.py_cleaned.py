import re
import string
import unicodedata
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from syntactic_unit import SyntacticUnit
class TextProcessor:
    def __init__(self):
        self.STOPWORDS = self.__load_stopwords(path="../stopwords.txt")
        self.LEMMATIZER = WordNetLemmatizer()
        self.STEMMER = SnowballStemmer("english")
        self.PUNCTUATION = re.compile('([%s])+' % re.escape(string.punctuation), re.UNICODE)
        self.NUMERIC = re.compile(r"[0-9]+", re.UNICODE)
        self.PAT_ALPHABETIC = re.compile('(((?![\d])\w)+)', re.UNICODE)
    def remove_punctuation(self, text):
        return self.PUNCTUATION.sub(" ", text)
    def remove_numeric(self, text):
        return self.NUMERIC.sub("", text)
    def remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.STOPWORDS]
    def stem_tokens(self, tokens):
        return [self.STEMMER.stem(word) for word in tokens]
    def lemmatize_tokens(self, tokens):
        if not tokens:
            return []
        if isinstance(tokens[0], str):
            pos_tags = pos_tag(tokens)
        else:
            pos_tags = tokens
        lemmatized_tokens = [
            self.LEMMATIZER.lemmatize(word[0]) if not self.__get_wordnet_pos(word[1])
            else self.LEMMATIZER.lemmatize(word[0], pos=self.__get_wordnet_pos(word[1]))
            for word in pos_tags
        ]
        return lemmatized_tokens
    def part_of_speech_tag(self, tokens):
        if isinstance(tokens, str):
            tokens = self.tokenize(tokens)
        return pos_tag(tokens)
    @staticmethod
    def __load_stopwords(path="stopwords.txt"):
        return list(set(stopwords.words('english')))
    @staticmethod
    def __get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None
    @staticmethod
    def deaccent(text):
        norm = unicodedata.normalize("NFD", text)
        result = "".join(ch for ch in norm if unicodedata.category(ch) != 'Mn')
        return unicodedata.normalize("NFC", result)
    def clean_text(self, text, filters=None, stem=False):
        text = text.lower()
        text = self.deaccent(text)
        text = self.remove_numeric(text)
        text = self.remove_punctuation(text)
        original_words = [match.group() for match in self.PAT_ALPHABETIC.finditer(text)]
        filtered_words = self.remove_stopwords(original_words)
        pos_tags = pos_tag(filtered_words)
        if stem:
            filtered_words = self.stem_tokens(filtered_words)
        else:
            filtered_words = self.lemmatize_tokens(pos_tags)
        units = [
            SyntacticUnit(word, word, tag)
            for i, (word, tag) in enumerate(pos_tags)
            if tag.startswith('N') and len(filtered_words[i]) >= 3
        ]
        return {unit.text: unit for unit in units}
    def tokenize(self, text):
        text = text.lower()
        text = self.deaccent(text)
        return [match.group() for match in self.PAT_ALPHABETIC.finditer(text)]
    def clean_sentence(self, text):
        text = text.lower()
        text = self.deaccent(text)
        text = self.remove_numeric(text)
        text = self.remove_punctuation(text)
        return text
