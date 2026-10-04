import encrypt
b1 = sys.argv[1]
b2 = sys.argv[2][1:]
b3 = sys.argv[3][1:]
b4 = sys.argv[4]
b5 = sys.argv[5][1:]
print(encrypt.enc(b1, b2, b3, b4, b5))