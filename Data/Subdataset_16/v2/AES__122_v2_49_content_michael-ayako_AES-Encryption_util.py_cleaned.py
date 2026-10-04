import logging
import random
def fonk1():
    logging.info("Configuring b2...")
    try:
        b1 = f"./chatterbot/logs{(__file__).split('.')[0]}.log"
        logging.basicConfig(b1 = b1, format='%(asctime)s %(message)s', filemode='w')
        b2 = logging.getLogger()
        b2.setLevel(logging.DEBUG)
        logging.info("Logger configured...")
    except Exception as err:
        logging.error(f"Logging not configured: {err}")
def fonk2(b1):
    try:
        with open(b1, 'rb'):
            pass
        logging.info(f"File {b1} was found")
    except Exception as err:
        logging.error(f"File check failed: {err}")
        exit()
def fonk3():
    print("Please select a random word from the list and share it with the receiver of this file by typing the number adjacent to the word")
    b3 = [random.randint(10000, 65535) for _ in range(6)]
    for idx, b9 in enumerate(b3):
        print(f"[{idx}] - {b9}")
    try:
        b4 = int(input())
        return b3[b4]
    except Exception as err:
        logging.error(f"Key generation failed: {err}")
        exit()
def fonk4(bits_matrix):
    b5 = [''.join(map(str, row)) for matrix in bits_matrix for row in matrix]
    b6 = [chr(int(bits, 2)) for bits in b5]
    with open('msg.enc', 'w', b7 = 'utf-8') as file:
        file.write(''.join(b6))
def fonk5(bits_matrix):
    b5 = [''.join(map(str, row)) for matrix in bits_matrix for row in matrix]
    b6 = [chr(int(bits, 2)) for bits in b5]
    with open('msg.txt', 'w', b7 = 'utf-8') as file:
        file.write(''.join(b6))
def fonk6():
    logging.info("Quitting")
    exit()
if b8 = = "__main__":
    fonk1()
    b1 = "example.txt"
    fonk2(b1)
    b9 = fonk3()
    print(f"Generated b9: {b9}")