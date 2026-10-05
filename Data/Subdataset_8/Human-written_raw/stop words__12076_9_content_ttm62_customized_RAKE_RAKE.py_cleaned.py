import os
import re
import string
import operator
from predefined_words import STOP_WORDS
def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False
def get_content(content_file):
    cleaned_data = []
    with open(content_file, encoding='utf-8') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    for line in content:
        cleaned_data.append(
            clean(line)
        )
    return cleaned_data
def clean(content):
    return re.sub(
        r'[^a-zA-Z0-9\s]'
        ,''
        ,content
    )
def load_stop_words(stop_word_file):
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "
            for word in line.split():
                stop_words.append(word)
    return stop_words
def separate_words(text, min_word_return_size):
    splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words
def split_sentences(text):
    sentence_delimiters = re.compile(u'[.!?;:\t\\\\"\\(\\)\\\u2019\u2013]|\\s\\-\\s')
    sentences = sentence_delimiters.split(text)
    return sentences
def build_stop_word_regex(stop_word_file_path, option='from_list'):
    if option == 'from_list':
        stop_word_list = STOP_WORDS
        stop_word_regex_list = []
        for word in stop_word_list:
            word_regex = r'\b' + word + r'(?![\w-])'
            stop_word_regex_list.append(word_regex)
        stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
        return stop_word_pattern
    else:
        stop_word_list = load_stop_words(stop_word_file_path)
        stop_word_regex_list = []
        for word in stop_word_list:
            word_regex = r'\b' + word + r'(?![\w-])'
            stop_word_regex_list.append(word_regex)
        stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
        return stop_word_pattern
def generate_candidate_keywords(sentence_list, stopword_pattern):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "":
                phrase_list.append(phrase)
    return phrase_list
def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = separate_words(phrase, 0)
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
def generate_candidate_keyword_scores(phrase_list, word_score):
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates
class Rake(object):
    def __init__(self, stop_words_path=''):
        if stop_words_path:
            if os.path.isfile(stop_words_path):
                self.stop_words_path = stop_words_path
                self.__stop_words_pattern = build_stop_word_regex(stop_words_path, option='')
            else:
                self.stop_words_path = stop_words_path
                self.__stop_words_pattern = build_stop_word_regex(stop_words_path, option='from_list')
        else:
            self.stop_words_path = stop_words_path
            self.__stop_words_pattern = build_stop_word_regex(stop_words_path, option='from_list')
    def run(self, content_file):
        if content_file:
            if os.path.isfile(content_file):
                sentence_list = get_content(content_file)
                phrase_list = generate_candidate_keywords(sentence_list, self.__stop_words_pattern)
                word_scores = calculate_word_scores(phrase_list)
                keyword_candidates = generate_candidate_keyword_scores(phrase_list, word_scores)
                sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)
                sorted_keywords_cut = [word for word in sorted_keywords if len( word[0].split() ) <= 3]
                return sorted_keywords_cut
            else:
                return []
        else:
            return []