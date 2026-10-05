import os
from toyecc import getcurvebyname, ECPrivateKey
def find_point_on_curve(curve, msg, msg_width_bits):
    int_message = int.from_bytes(msg, byteorder="little")
    for i in range(100):
        try_message = int_message | (i << msg_width_bits)
        point = curve.getpointwithx(try_message)
        if point:
            point = point[0]
            break
    return i + 1, point
def elgamal_encrypt(recipient_pubkey, msg, msg_width_bits):
    curve = recipient_pubkey.curve
    k = ECPrivateKey.generate(curve)
    C1 = k.pubkey.point
    C2 = k.scalar * recipient_pubkey.point
    trials, P_m = find_point_on_curve(curve, msg, msg_width_bits=msg_width_bits)
    ciphertext = C1, C2 + P_m
    return ciphertext
def elgamal_decrypt(recipient_privkey, ciphertext, msg_width_bits):
    curve = recipient_privkey.curve
    C1, C2 = ciphertext
    Cp = C1 * recipient_privkey.scalar
    P_m = C2 + (-Cp)
    int_message = int(P_m.x) & ((1 << msg_width_bits) - 1)
    msg = int.to_bytes(int_message, byteorder="little", length=(msg_width_bits + 7)
    return msg
curve = getcurvebyname("secp521r1")
privkey = ECPrivateKey.generate(curve)
pubkey = privkey.pubkey
message = b"foobar"
print("Message:", message)
ciphertext = elgamal_encrypt(pubkey, message, msg_width_bits=256)
print("Ciphertext:")
print("    C1 =", ciphertext[0])
print("    C2 =", ciphertext[1])
plaintext = elgamal_decrypt(privkey, ciphertext, msg_width_bits=256)
print("Plaintext:", plaintext)