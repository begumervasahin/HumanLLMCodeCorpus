
import bs4 as bs
import urllib.request
import re
import nltk
import heapq
nltk.download('stopwords')
nltk.download('punkt')
def fetch_wikipedia_article(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    text = "".join(paragraph.text for paragraph in soup.find_all('p'))
    return text
def preprocess_text(raw_text):
    text = re.sub(r'\[[0-9]*\]', ' ', raw_text)
    text = re.sub(r'\s+', ' ', text)
    clean_text = text.lower()
    clean_text = re.sub(r'\W', ' ', clean_text)
    clean_text = re.sub(r'\d', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return text, clean_text
def score_sentences(original_text, clean_text):
    sentences = nltk.sent_tokenize(original_text)
    stop_words = nltk.corpus.stopwords.words('english')
    word_counts = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            word_counts[word] = word_counts.get(word, 0) + 1
    max_count = max(word_counts.values())
    for word in word_counts:
        word_counts[word] = word_counts[word] / max_count
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_counts:
                if len(sentence.split()) < 25:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_counts[word]
    return sentence_scores
def summarize_article(url, num_sentences=5):
    raw_text = fetch_wikipedia_article(url)
    original_text, clean_text = preprocess_text(raw_text)
    sentence_scores = score_sentences(original_text, clean_text)
    best_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return best_sentences
if __name__ == '__main__':
    article_url = 'https:
    summary_sentences = summarize_article(article_url)
    print('------------------------------------------------------------')
    for sentence in summary_sentences:
        print(sentence)