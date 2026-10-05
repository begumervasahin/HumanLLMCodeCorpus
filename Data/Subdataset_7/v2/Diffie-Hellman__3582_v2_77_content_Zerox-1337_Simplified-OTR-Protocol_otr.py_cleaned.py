import hashlib
import socket
def fonk1(a, b1):
    if b1 = = 0:
        return 1, 0, a
    else:
        x, y, b2 = fonk1(b1, a % b1)
        return y, x - y * (a
def fonk2(a, m):
    x, y, b2 = fonk1(a, m)
    if b2 = = 1:
        return x % m
    else:
        return None
def fonk3(x):
    return x.to_bytes((x.bit_length() + 7)
def fonk4(b4):
    b3 = b1'eitn41 <3'
    b4 = fonk3(b4)
    return hashlib.sha1(b4 + b3).hexdigest()
def fonk5():
    b5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b5.connect(("eitn41.eit.lth.se", 1337))
    b6 = 'FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF'
    b7 = int(b6, 16)
    b4 = 2
    a1 = 2
    b8 = b5.recv(4096).decode('utf8').strip()
    b8 = int(b8, 16) % b7
    a2 = 4324
    b9 = pow(b4, a2, b7)
    b10 = format(b9, 'x')
    b5.send(b10.encode('utf8'))
    print('\ng_x2 is correct?', b5.recv(4096).decode('utf8').strip())
    print('All good in Auth?', b5.recv(4096).decode('utf8').strip())
    b11 = 'f6cf0a76b63bbba613a217b6d2f40c795756c4d8'
    b12 = int(b11, 16)
    b13 = b12 ^ g_xy
    b14 = format(b13, 'x')
    b5.send(b14.encode('utf8'))
    print('Msg answer:', b5.recv(4096).decode('utf8').strip())
    b5.close()
fonk5()