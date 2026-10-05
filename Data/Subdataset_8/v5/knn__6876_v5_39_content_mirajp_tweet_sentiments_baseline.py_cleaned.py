import re
from nltk.corpus import opinion_lexicon
def load_sentiment_words():
    sentiment_words = {}
    lexicon_words = opinion_lexicon.words()
    flag = 0
    for word in lexicon_words:
        if flag == 0:
            sentiment_words[word] = flag
            if re.search("zombie", word):
                flag = 1
        else:
            sentiment_words[word] = flag
    return sentiment_words
def classify_sentiment(test_file_path, out_file_path, sentiment_words):
    with open(test_file_path, 'r', encoding='ISO-8859-1') as test_file, open(out_file_path, 'w') as out_file:
        line_cnt = 1
        for tweet in test_file:
            words = tweet.split()
            neg = 0
            pos = 0
            for word in words:
                word_lower = word.lower()
                if word_lower in sentiment_words:
                    if sentiment_words[word_lower] == 1:
                        pos += 1
                    elif sentiment_words[word_lower] == 0:
                        neg += 1
            if pos > neg:
                out_file.write(f"{line_cnt} positive\n")
            elif pos < neg:
                out_file.write(f"{line_cnt} negative\n")
            else:
                out_file.write(f"{line_cnt} neutral\n")
            line_cnt += 1
if __name__ == "__main__":
    sentiment_words = load_sentiment_words()
    classify_sentiment("test.list", "baseline_out.txt", sentiment_words)