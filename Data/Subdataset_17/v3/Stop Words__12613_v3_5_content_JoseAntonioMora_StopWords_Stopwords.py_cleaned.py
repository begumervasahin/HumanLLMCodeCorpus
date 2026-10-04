import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def read_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        text = " ".join(line.strip() for line in file)
    return text
def tokenize_text(text):
    sentences = sent_tokenize(text)
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    return sentences, word_tokens
def display_sentence_tokens(sentences, word_tokens, sentence_number):
    sentence = sentences[sentence_number]
    tokens = word_tokens[sentence_number]
    print(f"\n[Sentence {sentence_number}] -> {sentence}\n")
    for i, token in enumerate(tokens):
        print(f"Token {i} -> {token}")
    print(f"\nTotal word tokens in sentence {sentence_number}: {len(tokens)} tokens")
    print(f"\nTotal sentences: {len(sentences) - 1}")
def main():
    file_path = 'texto.txt'
    text = read_file(file_path)
    sentences, word_tokens = tokenize_text(text)
    num_sentences = len(sentences)
    print(f"\nThe text contains {num_sentences} sentences.\nStarting from 0 to {num_sentences - 1}\n")
    try:
        sentence_number = int(input("Enter the sentence number: "))
    except ValueError:
        print("\n\nInvalid sentence number")
        return
    if 0 <= sentence_number < num_sentences:
        display_sentence_tokens(sentences, word_tokens, sentence_number)
    else:
        print("\n\nInvalid sentence number")
if __name__ == "__main__":
    main()