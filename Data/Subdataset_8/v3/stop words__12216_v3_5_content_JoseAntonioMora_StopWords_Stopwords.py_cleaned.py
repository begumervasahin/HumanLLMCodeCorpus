import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def read_text_file(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as archivo:
        return archivo.read().strip()
def tokenize_text(text):
    sentences = sent_tokenize(text)
    word_tokens = [word_tokenize(sentence) for sentence in sentences]
    return sentences, word_tokens
def display_sentence_info(sentences):
    num_sentences = len(sentences)
    print("\nEl texto contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(num_sentences, num_sentences - 1))
def display_sentence_tokens(sentence_tokens, sentence_number):
    print("\n[Sentencia {}] -> {}\n".format(sentence_number, sentence_tokens[sentence_number]))
    num_tokens = len(sentence_tokens[sentence_number])
    for index, token in enumerate(sentence_tokens[sentence_number]):
        print("Token {} -> {}".format(index, token))
    print("\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(sentence_number, num_tokens))
def main():
    texto = read_text_file('texto.txt')
    sentences, word_tokens = tokenize_text(texto)
    display_sentence_info(sentences)
    numero_sentencia = int(input("Ingresa el número de sentencia: "))
    if 0 < numero_sentencia < len(sentences):
        display_sentence_tokens(word_tokens, numero_sentencia)
        print("\nTotal de sentencias: {}".format(len(sentences) - 1))
    else:
        print("\n\nNúmero de sentencia no válido")
if __name__ == "__main__":
    main()