import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(file_path):
    with codecs.open(file_path, 'r', b1 = 'utf-8') as archivo:
        return archivo.read().strip()
def fonk2(text):
    b2 = sent_tokenize(text)
    b3 = [word_tokenize(sentence) for sentence in b2]
    return b2, b3
def fonk3(b2):
    b4 = len(b2)
    print("\nEl b6 contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(b4, b4 - 1))
def fonk4(sentence_tokens, sentence_number):
    print("\n[Sentencia {}] -> {}\n".format(sentence_number, sentence_tokens[sentence_number]))
    b5 = len(sentence_tokens[sentence_number])
    for index, token in enumerate(sentence_tokens[sentence_number]):
        print("Token {} -> {}".format(index, token))
    print("\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(sentence_number, b5))
def fonk5():
    b6 = fonk1('b6.txt')
    b2, b3 = fonk2(b6)
    fonk3(b2)
    b7 = int(input("Ingresa el número de sentencia: "))
    if 0 < b7 < len(b2):
        fonk4(b3, b7)
        print("\nTotal de sentencias: {}".format(len(b2) - 1))
    else:
        print("\n\nNúmero de sentencia no válido")
if b8 = = "__main__":
    fonk5()