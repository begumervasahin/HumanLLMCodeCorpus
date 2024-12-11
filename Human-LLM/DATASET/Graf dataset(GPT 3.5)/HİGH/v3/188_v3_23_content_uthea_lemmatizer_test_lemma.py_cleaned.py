class class1:
    def fonk1(self):
        self.b1 = {
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
    def fonk2(self, word):
        return self.b1.get(word, word)
b2 = class1()
b3 = [
    'bersetubuh', 'berdansa', 'penamaan', 'berusaha', 'berdansa', 'bolak-balik', 'gemetar',
    'petanggungjawaban', 'kepastian', 'berpendidikan', 'berhubungan', 'berwawasan', 'pengetahuan',
    'pengembala', 'penarikan', 'terbengkalai', 'rumahku', 'penanggulangan', 'perpecahan', 'pemalas',
    'tertikunganlah', 'perdamaian', 'terbirit-birit', 'cebokan', 'mengotomatisasikan', 'menyelesaikan',
    'sekawasan', 'pengertian', 'ketidakpastian'
]
b4 = [b2.fonk2(word) for word in b3]
print(*b4)