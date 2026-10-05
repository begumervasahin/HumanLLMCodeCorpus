import crypt
def generateHash(filename, outputfilename, salt):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                Hash = crypt.crypt(line, salt)
                result = " ".join([Hash, line])
                print result
                out.write(result + "\n")
def DESDictionary(filename,outputFile):
    plaintext = inputText(filename, outputFile)
def inputText(filename, outputfilename):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                if len(" ".join(line.split())) == 8:
                    print line
                    out.write(line)
if __name__ == "__main__":
    with open('rockyou.txt','r')as f:
        text = f.read()
    DESDictionary('rockyou.txt','pec1.txt')
    salt1='tl'
    salt2='as'
    generateHash('pec1.txt','hashed1.txt', salt1)
    generateHash('pec1.txt','hashed2.txt', salt2)