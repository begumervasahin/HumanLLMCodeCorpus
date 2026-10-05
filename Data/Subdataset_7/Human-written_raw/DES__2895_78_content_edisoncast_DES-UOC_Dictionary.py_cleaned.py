import crypt
def fonk1(filename, outputfilename, salt):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                b1 = crypt.crypt(line, salt)
                b2 = " ".join([b1, line])
                print b2
                out.write(b2 + "\n")
def fonk2(filename,outputFile):
    b3 = fonk3(filename, outputFile)
def fonk3(filename, outputfilename):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                if len(" ".join(line.split())) == 8:
                    print line
                    out.write(line)
if b4 = = "__main__":
    with open('rockyou.txt','r')as f:
        b5 = f.read()
    fonk2('rockyou.txt','pec1.txt')
    b6 = 'tl'
    b7 = 'as'
    fonk1('pec1.txt','hashed1.txt', b6)
    fonk1('pec1.txt','hashed2.txt', b7)