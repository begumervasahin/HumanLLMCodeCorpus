class ECDHE_RSA:
    def __init__(self, name):
        self.name = name
    def generate_rsa_key_pair(self):
        pass
    def generate_ec_key_pair(self):
        pass
    def generate_hash(self, data1, data2):
        pass
    def sign_with_rsa(self, data_hash, rsa_private_key, rsa_n):
        pass
    def verify_rsa_signature(self, signature, rsa_public_key, rsa_n, data_hash):
        pass
    def generate_shared_key(self, public_key, private_key):
        pass
    def is_point_on_curve(self, x, y):
        pass
def perform_key_exchange():
    matin = ECDHE_RSA("matin")
    mohamad = ECDHE_RSA("mohamad")
    ma_rsa_private, ma_rsa_public, ma_rsa_n = matin.generate_rsa_key_pair()
    mo_rsa_private, mo_rsa_public, mo_rsa_n = mohamad.generate_rsa_key_pair()
    ma_d, ma_dpub = matin.generate_ec_key_pair()
    mo_d, mo_dpub = mohamad.generate_ec_key_pair()
    ma_dpub_hash = matin.generate_hash(str(ma_dpub[0]), str(ma_dpub[1]))
    ma_sing_dpub = matin.sign_with_rsa(ma_dpub_hash, ma_rsa_private, ma_rsa_n)
    mo_dpub_hash = mohamad.generate_hash(str(mo_dpub[0]), str(mo_dpub[1]))
    mo_sing_dpub = mohamad.sign_with_rsa(mo_dpub_hash, mo_rsa_private, mo_rsa_n)
    mo_dpub_hash_recive = matin.generate_hash(str(mo_dpub[0]), str(mo_dpub[1]))
    sign_result_matin = matin.verify_rsa_signature(mo_sing_dpub, mo_rsa_public, mo_rsa_n, mo_dpub_hash_recive)
    ma_dpub_hash_recive = mohamad.generate_hash(str(ma_dpub[0]), str(ma_dpub[1]))
    sign_result_mohahmad = mohamad.verify_rsa_signature(ma_sing_dpub, ma_rsa_public, ma_rsa_n, ma_dpub_hash_recive)
    matin_share_key = matin.generate_shared_key(mo_dpub, ma_d)
    mohamad_share_key = mohamad.generate_shared_key(ma_dpub, mo_d)
    matin_curve_check = matin.is_point_on_curve(matin_share_key[0], matin_share_key[1])
    print("\n\nmatin verify rsa_sign:")
    print(sign_result_matin)
    print("\nmohamad verify rsa_sign:")
    print(sign_result_mohahmad)
    print("\nmatin share key:")
    print(matin_share_key)
    print("\nmohamad share key:")
    print(mohamad_share_key)
    print("\ncheck point in curve ?")
    print(matin_curve_check)
if __name__ == "__main__":
    perform_key_exchange()