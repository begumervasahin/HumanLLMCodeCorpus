import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def read_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        return " ".join(line.strip() for line in file)
def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return sentences, words
def display_sentence_info(sentences, words, sentence_number):
    print("\n[Sentencia {}] -> {}\n".format(sentence_number, sentences[sentence_number]))
    for idx, word in enumerate(words[sentence_number]):
        print("Token {} -> {}".format(idx, word))
    print("\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(
        sentence_number, len(words[sentence_number])))
    print("\nTotal de sentencias: {}".format(len(sentences) - 1))
def main():
    text = read_file('texto.txt')
    sentences, words = tokenize_text(text)
    print("\nEl texto contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(len(sentences), len(sentences) - 1))
    try:
        sentence_number = int(input("Ingresa el nÃºmero de sentencia: "))
    except ValueError:
        print("Entrada no vÃ¡lida. Por favor, ingresa un nÃºmero entero.")
        return
    if 0 <= sentence_number < len(sentences):
        display_sentence_info(sentences, words, sentence_number)
    else:
        print("\n\nNÃºmero de sentencia no vÃ¡lido")
if __name__ == "__main__":
    main()