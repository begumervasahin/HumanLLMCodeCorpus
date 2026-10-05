import os
import re
import operator
STOP_WORDS = set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
    "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
    "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
    "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's",
    "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours",
    "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these",
    "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until",
    "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd",
    "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
])
class Rake:
    def __init__(self, stop_words=None):
        self.stop_words = stop_words if stop_words else STOP_WORDS
    @staticmethod
    def is_number(s):
        try:
            float(s) if '.' in s else int(s)
            return True
        except ValueError:
            return False
    @staticmethod
    def clean(content):
        return re.sub(r'[^a-zA-Z0-9\s]', '', content)
    def get_content(self, content_file):
        cleaned_data = []
        with open(content_file, encoding='utf-8') as file:
            content = file.readlines()
        content = [x.strip() for x in content]
        for line in content:
            cleaned_data.append(self.clean(line))
        return cleaned_data
    def separate_words(self, text, min_word_return_size):
        splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        words = []
        for single_word in splitter.split(text):
            current_word = single_word.strip().lower()
            if len(current_word) > min_word_return_size and current_word != '' and not self.is_number(current_word):
                words.append(current_word)
        return words
    def split_sentences(self, text):
        sentence_delimiters = re.compile(u'[.!?;:\t\\\\"\\(\\)\\\u2019\u2013]|\\s\\-\\s')
        sentences = sentence_delimiters.split(text)
        return sentences
    def generate_candidate_keywords(self, sentence_list):
        phrase_list = []
        for s in sentence_list:
            tmp = re.sub(r'\b(' + '|'.join(self.stop_words) + r')\b', '|', s.strip().lower())
            phrases = tmp.split("|")
            for phrase in phrases:
                phrase = phrase.strip().lower()
                if phrase != "":
                    phrase_list.append(phrase)
        return phrase_list
    def calculate_word_scores(self, phrase_list):
        word_frequency = {}
        word_degree = {}
        for phrase in phrase_list:
            word_list = self.separate_words(phrase, 0)
            word_list_length = len(word_list)
            word_list_degree = word_list_length - 1
            for word in word_list:
                word_frequency.setdefault(word, 0)
                word_frequency[word] += 1
                word_degree.setdefault(word, 0)
                word_degree[word] += word_list_degree
        for item in word_frequency:
            word_degree[item] = word_degree[item] + word_frequency[item]
        word_score = {}
        for item in word_frequency:
            word_score.setdefault(item, 0)
            word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)
        return word_score
    def generate_candidate_keyword_scores(self, phrase_list, word_score):
        keyword_candidates = {}
        for phrase in phrase_list:
            keyword_candidates.setdefault(phrase, 0)
            word_list = self.separate_words(phrase, 0)
            candidate_score = 0
            for word in word_list:
                candidate_score += word_score[word]
            keyword_candidates[phrase] = candidate_score
        return keyword_candidates
    def run(self, content_file):
        if content_file and os.path.isfile(content_file):
            sentence_list = self.get_content(content_file)
            phrase_list = self.generate_candidate_keywords(sentence_list)
            word_scores = self.calculate_word_scores(phrase_list)
            keyword_candidates = self.generate_candidate_keyword_scores(phrase_list, word_scores)
            sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)
            sorted_keywords_cut = [word for word in sorted_keywords if len(word[0].split()) <= 3]
            return sorted_keywords_cut
        else:
            return []
if __name__ == "__main__":
    rake = Rake()
    content_file = "your_content_file.txt"
    keywords = rake.run(content_file)
    print(keywords)