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
    priv_key_a = 3426158395
    priv_key_b = 3479502846
    pub_key_g = 6748390294
    print(f'Public Key: {pub_key_g}')
    print(f'Private Key a: {priv_key_a}')
    print(f'Private Key b: {priv_key_b}')
    print(f'Verification Circle n: {n}')
    key_handler_a = KeyHandler(priv_key_a, pub_key_g, n)
    key_handler_b = KeyHandler(priv_key_b, pub_key_g, n)
    ag = key_handler_a.compute()
    bg = key_handler_b.compute()
    print(f'Private a and Public: {ag}')
    print(f'Private b and Public: {bg}')
    agb = key_handler_a.verify_key(bg)
    bga = key_handler_b.verify_key(ag)
    print(f'Combined agb: {agb}')
    print(f'Combined bga: {bga}')
if __name__ == '__main__':
    main()