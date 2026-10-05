import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
INPUT_FILE_PATH = 'CLEAN_AVA_FULL_COMMENTS.json'
OUTPUT_FILE_PATH = 'processed_comments.json'
def is_english(comment):
    try:
        return detect(comment) == 'en'
    except Exception as e:
        print(f"Error detecting language: {e}")
        return False
def normalize_text(text):
    text = re.sub(r'(.)\1+', r'\1\1', text)
    text = re.sub(r'[^\w\s,!.?]', '', text)
    return text
def filter_bad_words(tokens, bad_words):
    return [token for token in tokens if token.lower() not in bad_words]
def process_comments(input_path, output_path):
    processed_comments = []
    unigram_counts = Counter()
    bigram_counts = Counter()
    with open(input_path, 'r') as file:
        comments = json.load(file)
    for comment in comments:
        text = comment.get('comment', '')
        if is_english(text):
            normalized = normalize_text(text)
            tokens = word_tokenize(normalized)
            filtered = filter_bad_words(tokens, ['badword1', 'badword2'])
            unigram_counts.update(filtered)
            bigram_counts.update(ngrams(filtered, 2))
            processed_comments.append({'comment': ' '.join(filtered)})
    with open(output_path, 'w') as file:
        json.dump(processed_comments, file, indent=4)
process_comments(INPUT_FILE_PATH, OUTPUT_FILE_PATH)