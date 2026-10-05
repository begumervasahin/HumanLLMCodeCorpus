import hashlib
import socket
def extEuclideanAlg(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extEuclideanAlg(b, a % b)
        return y, x - y * (a
def modInvEuclid(a, m):
    x, y, gcd = extEuclideanAlg(a, m)
    if gcd == 1:
        return x % m
    else:
        return None
def convert_to_utf(x):
    return x.to_bytes((x.bit_length() + 7)
def h(g):
    passphrase = b'eitn41 <3'
    g = convert_to_utf(g)
    return hashlib.sha1(g + passphrase).hexdigest()
def run_ha4b2():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("eitn41.eit.lth.se", 1337))
    p_input = 'FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF'
    p = int(p_input, 16)
    g = 2
    g1 = 2
    g_x1 = int(soc.recv(4096).decode('utf8').strip(), 16) % p
    x2 = 4324
    g_x2 = pow(g, x2, p)
    soc.send(format(g_x2, 'x').encode('utf8'))
    print('\ng_x2 is correct?', soc.recv(4096).decode('utf8').strip())
    print('All good in Auth?', soc.recv(4096).decode('utf8').strip())
    msg = 'f6cf0a76b63bbba613a217b6d2f40c795756c4d8'
    msg_int = int(msg, 16)
    msg_e = msg_int ^ pow(g_x1, x2, p)
    soc.send(format(msg_e, 'x').encode('utf8'))
    print('Msg answer:', soc.recv(4096).decode('utf8').strip())
    soc.close()
run_ha4b2()