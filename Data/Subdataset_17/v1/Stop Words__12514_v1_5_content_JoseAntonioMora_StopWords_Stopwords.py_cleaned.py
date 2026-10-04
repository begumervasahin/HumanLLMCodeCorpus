import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def read_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        text = ""
        for line in file:
            text += " " + line.strip()
    return text
def tokenize_text(text):
    sentences = sent_tokenize(text)
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    return sentences, word_tokens
def main():
    file_path = 'texto.txt'
    text = read_file(file_path)
    sentences, word_tokens = tokenize_text(text)
    num_sentences = len(sentences)
    print("\nThe text contains {} sentences.\nStarting from 0 to {}\n".format(num_sentences, num_sentences - 1))
    try:
        sentence_number = int(input("Enter the sentence number: "))
    except ValueError:
        print("\n\nInvalid sentence number")
        return
    if 0 <= sentence_number < num_sentences:
        print("\n[Sentence {}] -> {}\n".format(sentence_number, sentences[sentence_number]))
        tokens = word_tokens[sentence_number]
        for i, token in enumerate(tokens):
            print("Token {} -> {}".format(i, token))
        print("\nTotal word tokens in sentence {}: {} tokens".format(sentence_number, len(tokens)))
        print("\nTotal sentences: {}".format(num_sentences - 1))
    else:
        print("\n\nInvalid sentence number")
if __name__ == "__main__":
    main()