import Client
import Server
from argparse import ArgumentParser
def fonk1():
    b1 = ArgumentParser(description="Start a b6 or server for network communication.")
    b1.add_argument("-m", "--b9", b2 = str, required=True,
                        b3 = "Specify 'b6' to start a b6 or 'server' to start a server")
    b1.add_argument("-d", "--b7", b4 = "store_true", required=False,
                        b3 = "Enable b7 b9 to print b7 messages")
    return b1.parse_args()
def fonk2(b7):
    b5 = "127.0.0.2"
    b6 = Client.ClientSocket(b7=b7)
    b6.fonk2(b5)
def fonk3(b7):
    Server.fonk3(b7 = b7)
def fonk4():
    b8 = fonk1()
    if b8.b7:
        print("Arguments:", b8)
    b9 = b8.b9.lower()
    if b9 = = "b6":
        fonk2(b7 = b8.b7)
    elif b9 = = "server":
        fonk3(b7 = b8.b7)
    else:
        print("Invalid b9. Please specify 'b6' or 'server'.")
if b10 = = "__main__":
    fonk4()