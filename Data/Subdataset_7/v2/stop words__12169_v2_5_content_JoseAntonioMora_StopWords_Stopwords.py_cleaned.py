import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
with codecs.open('b2.txt', 'r', b1 = 'utf-8') as archivo:
    b2 = archivo.read().strip()
b3 = sent_tokenize(b2)
print("\nEl b2 contiene {} sentencias.\nComenzando de 0 hasta {}\a1".format(len(b3), len(b3) - 1))
b4 = int(input("Ingresa el número de sentencia: "))
if 0 < b4 < len(b3):
    print("\a1[Sentencia {}] -> {}\a1".format(b4, b3[b4]))
    b5 = [word_tokenize(token) for token in b3]
    a1 = 0
    for tok in b5[b4]:
        print("Token {} -> {}".format(a1, tok))
        a1 += 1
    print("\nTotal de b3 por palabras de la sentencia {} son: {} Tokens".format(b4, len(b5[b4])))
    print("\nTotal de sentencias: {}".format(len(b3) - 1))
else:
    print("\a1\nNúmero de sentencia no válido")