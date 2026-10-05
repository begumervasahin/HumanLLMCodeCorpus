class KeyHandler:
    def __init__(self, private_key, public_key, verification_circle):
        self.private_key = private_key
        self.public_key = public_key
        self.verification_circle = verification_circle
    def compute_combined_key(self):
        return pow(self.public_key, self.private_key, self.verification_circle)
    def verify_combined_key(self, combined_key):
        return pow(combined_key, self.private_key, self.verification_circle)
def main():
    verification_circle = 100000
    private_key_a = 3426158395
    private_key_b = 3479502846
    public_key_g = 6748390294
    print('Public Key:', public_key_g)
    print('Private Key a:', private_key_a)
    print('Private Key b:', private_key_b)
    print('Verification Circle:', verification_circle)
    key_handler_a = KeyHandler(private_key_a, public_key_g, verification_circle)
    key_handler_b = KeyHandler(private_key_b, public_key_g, verification_circle)
    combined_key_a = key_handler_a.compute_combined_key()
    combined_key_b = key_handler_b.compute_combined_key()
    print('Combined Key of Private a and Public:', combined_key_a)
    print('Combined Key of Private b and Public:', combined_key_b)
    verification_result_agb = key_handler_a.verify_combined_key(combined_key_b)
    verification_result_bga = key_handler_b.verify_combined_key(combined_key_a)
    print('Verification Result for Combined Key agb:', verification_result_agb)
    print('Verification Result for Combined Key bga:', verification_result_bga)
if __name__ == '__main__':
    main()