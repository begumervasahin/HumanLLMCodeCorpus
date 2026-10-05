import json
from langdetect import detect
import re
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
input_file_path = 'CLEAN_AVA_FULL_COMMENTS.json'
output_file_path = 'processed_comments.json'
def is_comment_in_english(comment_text):
    try:
        return detect(comment_text) == 'en'
    except:
        return False
def normalize_comment_text(text):
    text = re.sub(r'(.)\1+', r'\1\1', text)
    text = re.sub(r'[^\w\s,!.?]', '', text)
    return text
def filter_tokens_by_bad_words(tokens, bad_words):
    return [token for token in tokens if token.lower() not in bad_words]
def process_comments(input_file_path, output_file_path):
    processed_comments = []
    unigram_counts = Counter()
    bigram_counts = Counter()
    with open(input_file_path, 'r') as file:
        comments_data = json.load(file)
    for item in comments_data:
        comment_text = item.get('comment', '')
        if is_comment_in_english(comment_text):
            normalized_text = normalize_comment_text(comment_text)
            tokens = word_tokenize(normalized_text)
            filtered_tokens = filter_tokens_by_bad_words(tokens, ['badword1', 'badword2'])
            unigram_counts.update(filtered_tokens)
            bigram_counts.update(ngrams(filtered_tokens, 2))
            processed_comments.append({'comment': ' '.join(filtered_tokens)})
    with open(output_file_path, 'w') as file:
        json.dump(processed_comments, file, indent=4)
process_comments(input_file_path, output_file_path)