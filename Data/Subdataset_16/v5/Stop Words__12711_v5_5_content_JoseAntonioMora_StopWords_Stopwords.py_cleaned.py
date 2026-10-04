import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
def fonk1(file_path):
    with codecs.open(file_path, 'r', b1 = 'utf-8') as file:
        return " ".join(line.strip() for line in file)
def fonk2(b4):
    b2 = sent_tokenize(b4)
    b3 = [word_tokenize(sentence) for sentence in b2]
    return b2, b3
def fonk3(b2, b3, b5):
    print("\n[Sentencia {}] -> {}\n".format(b5, b2[b5]))
    for idx, word in enumerate(b3[b5]):
        print("Token {} -> {}".format(idx, word))
    print("\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(
        b5, len(b3[b5])))
    print("\nTotal de sentencias: {}".format(len(b2) - 1))
def fonk4():
    b4 = fonk1('texto.txt')
    b2, b3 = fonk2(b4)
    print("\nEl texto contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(len(b2), len(b2) - 1))
    try:
        b5 = int(input("Ingresa el nÃºmero de sentencia: "))
    except ValueError:
        print("Entrada no vÃ¡lida. Por favor, ingresa un nÃºmero entero.")
        return
    if 0 <= b5 < len(b2):
        fonk3(b2, b3, b5)
    else:
        print("\n\nNÃºmero de sentencia no vÃ¡lido")
if b6 = = "__main__":
    fonk4()