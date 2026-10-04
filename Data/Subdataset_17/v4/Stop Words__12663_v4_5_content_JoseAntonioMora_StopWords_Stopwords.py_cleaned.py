import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
with codecs.open('texto.txt', 'r', encoding='utf-8') as archivo:
    texto = ""
    for linea in archivo:
        linea = linea.strip()
        texto += " " + linea
tokens = sent_tokenize(texto)
print("\nEl texto contiene {} sentencias.\nComenzando de 0 hasta {}\n".format(len(tokens), len(tokens) - 1))
try:
    numero_sentencia = int(input("Ingresa el nÃºmero de sentencia: "))
except ValueError:
    print("Entrada no vÃ¡lida. Por favor, ingresa un nÃºmero entero.")
    exit()
if 0 <= numero_sentencia < len(tokens):
    print("\n[Sentencia {}] -> {}\n".format(numero_sentencia, tokens[numero_sentencia]))
    word_tokens = [word_tokenize(token) for token in tokens]
    for n, tok in enumerate(word_tokens[numero_sentencia]):
        print("Token {} -> {}".format(n, tok))
    print("\nTotal de tokens por palabras de la sentencia {} son: {} Tokens".format(numero_sentencia, len(word_tokens[numero_sentencia])))
    print("\nTotal de sentencias: {}".format(len(tokens) - 1))
else:
    print("\n\nNÃºmero de sentencia no vÃ¡lido")