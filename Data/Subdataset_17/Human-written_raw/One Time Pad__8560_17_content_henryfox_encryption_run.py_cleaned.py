import encrypt
decryptOrEncrypt = sys.argv[1]
passpharse = sys.argv[2][1:]
path = sys.argv[3][1:]
outputType = sys.argv[4]
saveLocation = sys.argv[5][1:]
print(encrypt.enc(decryptOrEncrypt, passpharse, path, outputType, saveLocation))