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
if b5 = = "__main__":
    b6 = 'rockyou.txt'
    b7 = 'pec1.txt'
    b8 = 'hashed1.txt'
    b9 = 'hashed2.txt'
    b10 = 'tl'
    b11 = 'as'
    fonk2(b6, b7)
    fonk1(b7, b8, b10)
    fonk1(b7, b9, b11)