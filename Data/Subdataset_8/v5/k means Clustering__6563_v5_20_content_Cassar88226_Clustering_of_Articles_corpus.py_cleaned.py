import os
import subprocess
import codecs
import nltk
nltk_data_path = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_path):
    os.mkdir(nltk_data_path)
def get_pdf_paths(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            yield os.path.join(directory, filename)
pdf_directory = os.path.join(os.getcwd(), "pdf")
corpus_directory = os.path.join(os.getcwd(), "corpus")
def extract_text_from_pdfs(pdf_directory, corpus_directory):
    if not os.path.exists(corpus_directory):
        os.mkdir(corpus_directory)
    for pdf_path in get_pdf_paths(pdf_directory):
        pdf2txt_script = os.path.join(os.getcwd(), 'pdf2txt.py')
        text = subprocess.check_output(['python', pdf2txt_script, pdf_path])
        text = text.decode("utf-8")
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        text = text.replace(',', ' ')
        text = text.replace('-', '')
        text = text.replace(':', ' ')
        filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        output_path = os.path.join(corpus_directory, filename)
        with codecs.open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
extract_text_from_pdfs(pdf_directory, corpus_directory)
corpus_reader = nltk.corpus.PlaintextCorpusReader(corpus_directory, '.*\.txt')
word_freq = nltk.FreqDist(corpus_reader.words())
word_count = sum(word_freq.values())
vocab_size = len(word_freq)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} words and a total word count of {}.".format(vocab_size, word_count))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", word_freq.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", word_freq.most_common())
print('----------------------------------------------------------------------')