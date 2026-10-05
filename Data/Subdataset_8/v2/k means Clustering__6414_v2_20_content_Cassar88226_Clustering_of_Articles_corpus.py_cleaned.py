import os
import nltk
import codecs
import subprocess
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def get_pdf_documents(path):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
def extract_pdf_corpus(pdf_folder, corpus_folder):
    create_directory(corpus_folder)
    for pdf_path in get_pdf_documents(pdf_folder):
        pdf2txt_path = os.path.join(os.getcwd(), 'pdf2txt.py')
        text = subprocess.check_output(['python', pdf2txt_path, pdf_path])
        filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        output_path = os.path.join(corpus_folder, filename)
        text = text.decode("utf-8")
        text = text.replace('\n', ' ').replace('\r', ' ').replace(',', ' ').replace('-', '').replace(':', ' ')
        with codecs.open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
PDF_FOLDER = os.path.join(os.getcwd(), "pdf")
CORPUS_FOLDER = os.path.join(os.getcwd(), "corpus")
extract_pdf_corpus(PDF_FOLDER, CORPUS_FOLDER)
corpus_reader = nltk.corpus.PlaintextCorpusReader(CORPUS_FOLDER, '.*\.txt')
word_freq_dist = nltk.FreqDist(corpus_reader.words())
total_word_count = sum(word_freq_dist.values())
vocab_size = len(word_freq_dist)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(total_word_count, vocab_size))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", word_freq_dist.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", word_freq_dist.most_common(10))
print('----------------------------------------------------------------------')