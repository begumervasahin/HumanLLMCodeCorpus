from Crypto.PublicKey import ECC
import ecc_simple
def format(eccPoint):
    return (int(eccPoint.x),int(eccPoint.y))
keyA = ECC.generate(curve='P-256')
keyB = ECC.generate(curve='P-256')
privateA = keyA.d
privateB = keyB.d
publicA = keyA.pointQ
publicB = keyB.pointQ
shared_keyA = format(publicB * privateA)
shared_keyB = format(publicA * privateB)
ecc_simple.set_p256_param()
g = ecc_simple.g
publicA_1 = ecc_simple.times(int(privateA), g)
publicB_1 = ecc_simple.times(int(privateB), g)
shared_keyA_1 = ecc_simple.times(int(privateA), publicB_1)
shared_keyB_1 = ecc_simple.times(int(privateA), publicB_1)
print publicA_1