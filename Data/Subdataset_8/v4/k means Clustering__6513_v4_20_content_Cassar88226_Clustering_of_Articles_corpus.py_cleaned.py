import os
import subprocess
import codecs
import nltk
nltk_data_path = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_path):
    os.mkdir(nltk_data_path)
def get_pdf_docs(path):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
pdf_docs_path = os.path.join(os.getcwd(), "pdf")
corpus_path = os.path.join(os.getcwd(), "corpus")
def extract_pdf_corpus(pdf_path, corpus_path):
    if not os.path.exists(corpus_path):
        os.mkdir(corpus_path)
    for path in get_pdf_docs(pdf_path):
        pdf2txt_script = os.path.join(os.getcwd(), 'pdf2txt.py')
        document = subprocess.check_output(['python', pdf2txt_script, path])
        document = document.decode("utf-8")
        document = document.replace('\n', ' ')
        document = document.replace('\r', ' ')
        document = document.replace(',', ' ')
        document = document.replace('-', '')
        document = document.replace(':', ' ')
        document = str(document)
        filename = os.path.splitext(os.path.basename(path))[0] + ".txt"
        output_path = os.path.join(corpus_path, filename)
        with codecs.open(output_path, 'w', encoding='utf-8') as f:
            f.write(document)
extract_pdf_corpus(pdf_docs_path, corpus_path)
kdd_corpus = nltk.corpus.PlaintextCorpusReader(corpus_path, '.*\.txt')
word_freq = nltk.FreqDist(kdd_corpus.words())
word_count = sum(word_freq.values())
vocab_size = len(word_freq)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(word_count, vocab_size))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", word_freq.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", word_freq.most_common())
print('----------------------------------------------------------------------')