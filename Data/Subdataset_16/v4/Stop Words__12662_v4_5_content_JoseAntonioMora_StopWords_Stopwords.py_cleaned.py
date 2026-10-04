import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
with codecs.open('b2.txt', 'r', b1 = 'utf-8') as archivo:
    b2 = ""
    for b3 in archivo:
        b3 = b3.strip()
        b2 += " " + b3
b4 = sent_tokenize(b2)
print("\nEl b2 contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(len(b4), len(b4) - 1))
try:
    b5 = int(input("Ingresa el nÃºmero de sentencia: "))
except ValueError:
    print("Entrada no vÃ¡lida. Por favor, ingresa un nÃºmero entero.")
    exit()
if 0 <= b5 < len(b4):
    print("\n[Sentencia {}] -> {}\n".format(b5, b4[b5]))
    b6 = [word_tokenize(token) for token in b4]
    for n, tok in enumerate(b6[b5]):
        print("Token {} -> {}".format(n, tok))
    print("\nTotal de b4 por palabras de la sentencia {} son: {} Tokens".format(b5, len(b6[b5])))
    print("\nTotal de sentencias: {}".format(len(b4) - 1))
else:
    print("\n\nNÃºmero de sentencia no vÃ¡lido")