
from lemmatizer import Lemmatizer
b1 = Lemmatizer()
b2 = [
    'bersetubuh', 'berdansa', 'penamaan', 'berusaha', 'berdansa', 'bolak-balik',
    'gemetar', 'petanggungjawaban', 'kepastian', 'berpendidikan', 'berhubungan',
    'berwawasan', 'pengetahuan', 'pengembala', 'penarikan', 'terbengkalai', 'rumahku',
    'penanggulangan', 'perpecahan', 'pemalas', 'tertikunganlah', 'perdamaian',
    'terbirit-birit', 'cebokan', 'mengotomatisasikan', 'menyelesaikan', 'sekawasan',
    'pengertian', 'ketidakpastian'
]
for word in b2:
    b3 = b1.lemmatize(word)
    print(word, b3)