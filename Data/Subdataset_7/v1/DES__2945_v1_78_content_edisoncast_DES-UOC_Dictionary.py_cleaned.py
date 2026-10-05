import crypt
def fonk1(filename, outputfilename, salt):
    with open(outputfilename, "w") as out:
        with open(filename, 'r') as f:
            for line in f:
                b1 = crypt.crypt(line.strip(), salt)
                b2 = f"{b1} {line}"
                print(b2)
                out.write(b2 + "\n")
def fonk2(filename, outputfilename):
    fonk3(filename, outputfilename)
def fonk3(filename, outputfilename):
    with open(outputfilename, "w") as out:
        with open(filename, 'r') as f:
            for line in f:
                if len(line.strip()) == 8:
                    print(line)
                    out.write(line)
if b3 = = "__main__":
    with open('rockyou.txt', 'r') as f:
        b4 = f.read()
    fonk2('rockyou.txt', 'pec1.txt')
    b5 = 'tl'
    b6 = 'as'
    fonk1('pec1.txt', 'hashed1.txt', b5)
    fonk1('pec1.txt', 'hashed2.txt', b6)