import os
import subprocess
import codecs
import nltk
nltk_data_path = os.path.expanduser('~/nltk_data')
os.makedirs(nltk_data_path, exist_ok=True)
print("Does nltk_data path exist:", os.path.exists(nltk_data_path))
DOCS_PDF = os.path.join(os.getcwd(), "pdf")
CORPUS = os.path.join(os.getcwd(), "corpus")
def get_pdf_docs(path=DOCS_PDF):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
pdf_docs = list(get_pdf_docs())
print(f"Number of PDF documents found: {len(pdf_docs)}")
def extract_pdf_corpus(DOCS_PDF=DOCS_PDF, corpus_dir=CORPUS):
    os.makedirs(corpus_dir, exist_ok=True)
    for pdf_path in get_pdf_docs(DOCS_PDF):
        pdf2txt_script = os.path.join(os.getcwd(), 'pdf2txt.py')
        document = subprocess.check_output(['python', pdf2txt_script, pdf_path])
        txt_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        txt_path = os.path.join(corpus_dir, txt_filename)
        document_text = document.decode("utf-8").replace('\n', ' ').replace('\r', ' ')
        document_text = document_text.replace(',', ' ').replace('-', '').replace(':', ' ')
        with codecs.open(txt_path, 'w', encoding='utf-8') as f:
            f.write(document_text)
extract_pdf_corpus()
kdd_corpus = nltk.corpus.PlaintextCorpusReader(CORPUS, '.*\.txt')
words_freq_dist = nltk.FreqDist(kdd_corpus.words())
total_word_count = sum(words_freq_dist.values())
vocabulary_size = len(words_freq_dist)
print('----------------------------------------------------------------------')
print(f"Corpus contains a vocabulary of {vocabulary_size} and a word count of {total_word_count}.")
print('----------------------------------------------------------------------')
print("Hapaxes (words that appear only once):")
print(words_freq_dist.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:")
print(words_freq_dist.most_common())