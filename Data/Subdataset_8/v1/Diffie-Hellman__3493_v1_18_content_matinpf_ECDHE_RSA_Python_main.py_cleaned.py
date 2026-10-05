class ECDHE_RSA:
    def __init__(self, name):
        self.name = name
    def rsakeygenarate(self):
        pass
    def gen_ECkeypair(self):
        pass
    def hash_info(self, data1, data2):
        pass
    def ras_sign(self, data_hash, rsa_private, rsa_n):
        pass
    def rsa_verification(self, signature, rsa_public, rsa_n, data_hash):
        pass
    def gen_ECkeyAg(self, public_key, private_key):
        pass
    def in_Curve(self, x, y):
        pass
matin = ECDHE_RSA("matin")
mohamad = ECDHE_RSA("mohamad")
ma_rsa_private, ma_rsa_public, ma_rsa_n = matin.rsakeygenarate()
mo_rsa_private, mo_rsa_public, mo_rsa_n = mohamad.rsakeygenarate()
ma_d, ma_dpub = matin.gen_ECkeypair()
mo_d, mo_dpub = mohamad.gen_ECkeypair()
ma_dpub_hash = matin.hash_info(str(ma_dpub[0]), str(ma_dpub[1]))
ma_sing_dpub = matin.ras_sign(ma_dpub_hash, ma_rsa_private, ma_rsa_n)
mo_dpub_hash = mohamad.hash_info(str(mo_dpub[0]), str(mo_dpub[1]))
mo_sing_dpub = mohamad.ras_sign(mo_dpub_hash, mo_rsa_private, mo_rsa_n)
mo_dpub_hash_recive = matin.hash_info(str(mo_dpub[0]), str(mo_dpub[1]))
sign_result_matin = matin.rsa_verification(mo_sing_dpub, mo_rsa_public, mo_rsa_n, mo_dpub_hash_recive)
ma_dpub_hash_recive = mohamad.hash_info(str(ma_dpub[0]), str(ma_dpub[1]))
sign_result_mohahmad = mohamad.rsa_verification(ma_sing_dpub, ma_rsa_public, ma_rsa_n, ma_dpub_hash_recive)
matin_sharekey = matin.gen_ECkeyAg(mo_dpub, ma_d)
mohamad_sharekey = mohamad.gen_ECkeyAg(ma_dpub, mo_d)
matin_curve_check = matin.in_Curve(matin_sharekey[0], matin_sharekey[1])
print("\n\nmatin verify rsa_sign:")
print(sign_result_matin)
print("\nmohamad verify rsa_sign:")
print(sign_result_mohahmad)
print("\nmatin share key:")
print(matin_sharekey)
print("\nmohamad share key:")
print(mohamad_sharekey)
print("\ncheck point in curve ?")
print(matin_curve_check)