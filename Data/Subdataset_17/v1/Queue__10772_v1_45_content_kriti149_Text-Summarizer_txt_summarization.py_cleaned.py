
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
    text = ""
    for paragraph in soup.find_all('p'):
        text += paragraph.text
    return text
def preprocess_text(text):
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    clean_text = text.lower()
    clean_text = re.sub(r'\W', ' ', clean_text)
    clean_text = re.sub(r'\d', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return text, clean_text
def score_sentences(text, clean_text):
    sentences = nltk.sent_tokenize(text)
    stop_words = nltk.corpus.stopwords.words('english')
    word2count = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            if word not in word2count:
                word2count[word] = 1
            else:
                word2count[word] += 1
    max_count = max(word2count.values())
    for word in word2count:
        word2count[word] = word2count[word] / max_count
    sent2score = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word2count:
                if len(sentence.split()) < 25:
                    if sentence not in sent2score:
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]
    return sent2score
def summarize_article(url, n=5):
    text = fetch_wikipedia_article(url)
    text, clean_text = preprocess_text(text)
    sent2score = score_sentences(text, clean_text)
    best_sentences = heapq.nlargest(n, sent2score, key=sent2score.get)
    return best_sentences
if __name__ == '__main__':
    article_url = 'https:
    summary_sentences = summarize_article(article_url)
    print('------------------------------------------------------------')
    for sentence in summary_sentences:
        print(sentence)