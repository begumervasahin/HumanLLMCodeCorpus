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
    print(f"Public Key: {pub_key_g}")
    print(f"Private Key a: {priv_key_a}")
    print(f"Private Key b: {priv_key_b}")
    print(f"Verification Circle n: {n}")
    key_handler_a = KeyHandler(priv_key_a, pub_key_g, n)
    key_handler_b = KeyHandler(priv_key_b, pub_key_g, n)
    result_a_public = key_handler_a.compute()
    result_b_public = key_handler_b.compute()
    print(f"Private a and Public: {result_a_public}")
    print(f"Private b and Public: {result_b_public}")
    combined_a_b = key_handler_a.verify_key(result_b_public)
    combined_b_a = key_handler_b.verify_key(result_a_public)
    print(f"Combined a with b's public key: {combined_a_b}")
    print(f"Combined b with a's public key: {combined_b_a}")
if __name__ == '__main__':
    main()