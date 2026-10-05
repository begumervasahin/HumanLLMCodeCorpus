
import codecs
import win_unicode_console
from nltk.tokenize import sent_tokenize, word_tokenize
win_unicode_console.enable()
archivo = codecs.open('texto.txt', 'r', encoding='utf-8')
texto = ""
for linea in archivo:
    linea = linea.strip()
    texto = texto + " " + linea
tokens = sent_tokenize(texto)
print("\nThe text contains {} sentences.".format(len(tokens)))
print("Numbered from 0 to {}\n".format(len(tokens) - 1))
numero_sentencia = int(input("Enter the sentence number: "))
if 0 < numero_sentencia < len(tokens):
    print("\n[Sentence {}] -> {}\n".format(numero_sentencia, tokens[numero_sentencia]))
    word_tokens = word_tokenize(tokens[numero_sentencia])
    for index, token in enumerate(word_tokens):
        print("Token {} -> {}".format(index, token))
    print("\nTotal word tokens in sentence {}: {}".format(numero_sentencia, len(word_tokens)))
    print("Total sentences: {}\n".format(len(tokens) - 1))
else:
    print("\nInvalid sentence number. Please enter a valid number.")