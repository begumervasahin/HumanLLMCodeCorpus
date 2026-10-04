import crypt
def fonk1(input_filename, output_filename, salt):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for b1 in infile:
            b1 = b1.strip()
            if b1:
                b2 = crypt.crypt(b1, salt)
                b3 = f"{b2} {b1}"
                print(b3)
                outfile.write(b3 + "\n")
def fonk2(input_filename, output_filename, b4 = 8):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for b1 in infile:
            b1 = b1.strip()
            if len(b1) == b4:
                print(b1)
                outfile.write(b1 + "\n")
def fonk3():
    b5 = 'rockyou.txt'
    b6 = 'pec1.txt'
    b7 = 'hashed1.txt'
    b8 = 'hashed2.txt'
    b9 = 'tl'
    b10 = 'as'
    fonk2(b5, b6)
    fonk1(b6, b7, b9)
    fonk1(b6, b8, b10)
if b11 = = "__main__":
    fonk3()