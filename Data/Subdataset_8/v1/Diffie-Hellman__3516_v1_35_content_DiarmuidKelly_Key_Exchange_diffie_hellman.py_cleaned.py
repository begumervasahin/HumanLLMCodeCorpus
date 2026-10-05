class KeyHandler:
    def __init__(self, priv_key, pub_key, n):
        self.priv_key = priv_key
        self.pub_key = pub_key
        self.n = n
    def compute(self):
        return pow(self.pub_key, self.priv_key, self.n)
    def verify_key(self, combined_key):
        return pow(combined_key, self.priv_key, self.n)
def main():
    n = 100000
    a = 3426158395
    b = 3479502846
    g = 6748390294
    print('Public Key:', g)
    print('Private Key a:', a)
    print('Private Key b:', b)
    print('Verification Circle n:', n)
    key_handler1 = KeyHandler(a, g, n)
    key_handler2 = KeyHandler(b, g, n)
    ag = key_handler1.compute()
    bg = key_handler2.compute()
    print('Private a and Public:', ag)
    print('Private b and Public:', bg)
    agb = key_handler1.verify_key(bg)
    bga = key_handler2.verify_key(ag)
    print('Combined agb:', agb)
    print('Combined bga:', bga)
if __name__ == '__main__':
    main()