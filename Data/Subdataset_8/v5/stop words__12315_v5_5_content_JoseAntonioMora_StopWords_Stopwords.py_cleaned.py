import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def read_text_from_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        return ' '.join(line.strip() for line in file)
def tokenize_text(text):
    sentences = sent_tokenize(text)
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    return sentences, word_tokens
def display_sentence_info(sentences):
    num_sentences = len(sentences)
    print(f"\nThe text contains {num_sentences} sentences.")
    print(f"Numbered from 0 to {num_sentences - 1}\n")
def display_sentence_and_tokens(sentence_index, sentences, word_tokens):
    selected_sentence = sentences[sentence_index]
    print(f"\n[Sentence {sentence_index}] -> {selected_sentence}\n")
    tokens = word_tokens[sentence_index]
    for index, token in enumerate(tokens):
        print(f"Token {index} -> {token}")
    print(f"\nTotal word tokens in sentence {sentence_index}: {len(tokens)}")
def main():
    file_path = 'texto.txt'
    text = read_text_from_file(file_path)
    sentences, word_tokens = tokenize_text(text)
    display_sentence_info(sentences)
    sentence_index = int(input("Enter the sentence number: "))
    if 0 < sentence_index < len(sentences):
        display_sentence_and_tokens(sentence_index, sentences, word_tokens)
        print(f"Total sentences: {len(sentences)}\n")
    else:
        print("\nInvalid sentence number. Please enter a valid number.")
if __name__ == "__main__":
    main()