import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
maxRandomNumber = 500
fileToRead = 'in.txt'
outFile = 'crypted.txt'
outFile2 = 'decrypted.txt'
def readFromFile(file):
    with io.open(file, "r+", encoding="utf-8") as myFile:
        data = myFile.read()
    return data
def main():
    with io.open(outFile, "w", encoding="utf-8") as out, io.open(outFile2, "w", encoding="utf-8") as out2:
        random1 = generateRandomNumber(maxRandomNumber)
        random2 = generateRandomNumber(maxRandomNumber)
        prime1 = findNearPrime(random1)
        prime2 = findNearPrime(random2)
        privKey, pubKey = generateKeys(prime1, prime2)
        print("Private Key:", privKey)
        print("Public Key:", pubKey)
        textToEncrypt = readFromFile(fileToRead)
        encryptedData = encrypt(textToEncrypt, privKey)
        print("Encrypted data:", encryptedData)
        out.write(encryptedData)
        decryptedData = decrypt(encryptedData, pubKey)
        out2.write(decryptedData)
if __name__ == "__main__":
    main()