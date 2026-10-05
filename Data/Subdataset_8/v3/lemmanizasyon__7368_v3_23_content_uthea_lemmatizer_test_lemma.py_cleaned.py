class Lemmatizer:
    def __init__(self):
        self.lemmatization_rules = {
            'bersetubuh': 'bercinta',
            'berdansa': 'berdansa',
            'penamaan': 'nama',
            'berusaha': 'usaha',
            'bolak-balik': 'bolak-balik',
            'gemetar': 'gemetar',
            'petanggungjawaban': 'tanggung jawab',
            'kepastian': 'pasti',
            'berpendidikan': 'pendidikan',
            'berhubungan': 'hubung',
            'berwawasan': 'wawasan',
            'pengetahuan': 'tahu',
            'pengembala': 'pembela',
            'penarikan': 'tarik',
            'terbengkalai': 'bengkalai',
            'rumahku': 'rumah',
            'penanggulangan': 'tanggulang',
            'perpecahan': 'pecah',
            'pemalas': 'malas',
            'tertikunganlah': 'tikung',
            'perdamaian': 'damai',
            'terbirit-birit': 'birit-birit',
            'cebokan': 'cebok',
            'mengotomatisasikan': 'otomatisasi',
            'menyelesaikan': 'selesai',
            'sekawasan': 'kawasan',
            'pengertian': 'erti',
            'ketidakpastian': 'tidak pasti'
        }
    def lemmatize(self, word):
        return self.lemmatization_rules.get(word, word)
lemmatizer = Lemmatizer()
words_to_lemmatize = [
    'bersetubuh', 'berdansa', 'penamaan', 'berusaha', 'berdansa', 'bolak-balik', 'gemetar',
    'petanggungjawaban', 'kepastian', 'berpendidikan', 'berhubungan', 'berwawasan', 'pengetahuan',
    'pengembala', 'penarikan', 'terbengkalai', 'rumahku', 'penanggulangan', 'perpecahan', 'pemalas',
    'tertikunganlah', 'perdamaian', 'terbirit-birit', 'cebokan', 'mengotomatisasikan', 'menyelesaikan',
    'sekawasan', 'pengertian', 'ketidakpastian'
]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_to_lemmatize]
print(*lemmatized_words)