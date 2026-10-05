import crypt
def fonk1(input_filename, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                b1 = crypt.crypt(line.strip(), salt)
                b2 = f"{b1} {line}"
                print(b2)
                output_file.write(b2 + "\n")
def fonk2(input_filename, output_filename):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                if len(line.strip()) == 8:
                    print(line)
                    output_file.write(line)
def fonk3():
    b3 = 'rockyou.txt'
    b4 = 'pec1.txt'
    DESDictionary(b3, b4)
    b5 = 'tl'
    b6 = 'as'
    generateHash(b4, 'hashed1.txt', b5)
    generateHash(b4, 'hashed2.txt', b6)
if b7 = = "__main__":
    fonk3()