
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
def clean_text(text):
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    clean_text = text.lower()
    clean_text = re.sub(r'\W', ' ', clean_text)
    clean_text = re.sub(r'\d', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text
def score_sentences(sentences, word2count):
    sent2score = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word2count:
                if len(sentence.split(' ')) < 25:
                    if sentence not in sent2score:
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]
    return sent2score
def main():
    article_url = 'https:
    raw_text = fetch_wikipedia_article(article_url)
    clean_text_content = clean_text(raw_text)
    sentences = nltk.sent_tokenize(raw_text)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word2count = {}
    for word in nltk.word_tokenize(clean_text_content):
        if word not in stop_words:
            if word not in word2count:
                word2count[word] = 1
            else:
                word2count[word] += 1
    max_freq = max(word2count.values())
    for word in word2count:
        word2count[word] = word2count[word] / max_freq
    sent2score = score_sentences(sentences, word2count)
    best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
    print('------------------------------------------------------------')
    for sentence in best_sentences:
        print(sentence)
if __name__ == '__main__':
    main()