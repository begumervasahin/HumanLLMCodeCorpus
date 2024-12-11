import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
win_unicode_console.enable()
b1 = codecs.open('b2.txt', 'r', encoding='utf-8')
b2 = ""
for b3 in b1:
    b3 = b3.strip()
    b2 = b2 + " " + b3
b4 = sent_tokenize(b2)
print "\nEl b2 contine {} sentencias.\nComenzando de 0 hasta {}\a1".format(len(b4), len(b4) - 1)
b5 = input("Ingresa en numero de sentencia: ")
if(b5 > 0 and b5 < len(b4)):
    print "\a1[Sentencia " + str(b5) + "] -> " + b4[b5], '\a1'
    b6 = []
    for token in b4:
        b6.append(word_tokenize(token))
    a1 = 0
    for tok in b6[b5]:
        print "Token " + str(a1) + " -> " + tok
        a1 = a1 + 1
    print "\nTotal de b4 por palabras de la sentencia {} son: {} Tokens".format(b5, len(b6[b5]))
    print "\nTotal de sentencias: {}".format(len(b4) - 1)
else:
    print "\a1\nNumero de sentencia no valido"