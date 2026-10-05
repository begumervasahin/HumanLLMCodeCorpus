import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
input_file = 'CLEAN_AVA_FULL_COMMENTS.json'
output_file = 'processed_comments.json'
def is_english(comment):
    try:
        return detect(comment) == 'en'
    except:
        return False
def normalize_text(text):
    text = re.sub(r'(.)\1+', r'\1\1', text)
    text = re.sub(r'[^\w\s,!.?]', '', text)
    return text
def tokenize_and_filter(text, bad_words):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.lower() not in bad_words]
    return tokens
def process_comments(input_file, output_file):
    processed_comments = []
    unigram_counts = Counter()
    bigram_counts = Counter()
    with open(input_file, 'r') as f:
        comments_data = json.load(f)
    for item in comments_data:
        comment = item.get('comment', '')
        if is_english(comment):
            normalized_comment = normalize_text(comment)
            tokens = tokenize_and_filter(normalized_comment, ['badword1', 'badword2'])
            unigram_counts.update(tokens)
            bigram_counts.update(ngrams(tokens, 2))
            processed_comments.append({'comment': ' '.join(tokens)})
    with open(output_file, 'w') as f:
        json.dump(processed_comments, f, indent=4)
process_comments(input_file, output_file)