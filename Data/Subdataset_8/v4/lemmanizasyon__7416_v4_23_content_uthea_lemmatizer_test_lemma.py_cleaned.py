
from lemmatizer import Lemmatizer
lemma = Lemmatizer()
words_to_lemmatize = [
    'bersetubuh', 'berdansa', 'penamaan', 'berusaha', 'berdansa', 'bolak-balik',
    'gemetar', 'petanggungjawaban', 'kepastian', 'berpendidikan', 'berhubungan',
    'berwawasan', 'pengetahuan', 'pengembala', 'penarikan', 'terbengkalai', 'rumahku',
    'penanggulangan', 'perpecahan', 'pemalas', 'tertikunganlah', 'perdamaian',
    'terbirit-birit', 'cebokan', 'mengotomatisasikan', 'menyelesaikan', 'sekawasan',
    'pengertian', 'ketidakpastian'
]
for word in words_to_lemmatize:
    lemmatized_word = lemma.lemmatize(word)
    print(word, lemmatized_word)