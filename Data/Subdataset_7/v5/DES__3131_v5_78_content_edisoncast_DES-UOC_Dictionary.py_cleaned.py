import crypt
def fonk1(input_filename, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                b1 = line.strip()
                b2 = crypt.crypt(b1, salt)
                b3 = f"{b2} {b1}"
                print(b3)
                output_file.write(b3 + "\n")
def fonk2(input_filename, output_filename):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                b1 = line.strip()
                if len(b1) == 8:
                    print(b1)
                    output_file.write(b1 + '\n')
def fonk3(input_filename, output_filename):
    fonk2(input_filename, output_filename)
def fonk4():
    b4 = 'rockyou.txt'
    b5 = 'pec1.txt'
    fonk3(b4, b5)
    b6 = 'tl'
    b7 = 'as'
    fonk1(b5, 'hashed1.txt', b6)
    fonk1(b5, 'hashed2.txt', b7)
if b8 = = "__main__":
    fonk4()