import crypt
def fonk1(b5, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(b5, 'r') as input_file:
            for b1 in input_file:
                b1 = b1.strip()
                b2 = crypt.crypt(b1, salt)
                b3 = f"{b2} {b1}\n"
                print(b3)
                output_file.write(b3)
def fonk2(b5, output_filename):
    with open(output_filename, "w") as output_file:
        with open(b5, 'r') as input_file:
            for b1 in input_file:
                b1 = b1.strip()
                if len(b1) == 8:
                    print(b1)
                    output_file.write(b1 + '\n')
if b4 = = "__main__":
    b5 = 'rockyou.txt'
    b6 = 'pec1.txt'
    b7 = 'hashed1.txt'
    b8 = 'hashed2.txt'
    fonk2(b5, b6)
    b9 = 'tl'
    b10 = 'as'
    fonk1(b6, b7, b9)
    fonk1(b6, b8, b10)